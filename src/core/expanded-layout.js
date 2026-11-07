// Geometry for expanded scenes. Coordinates come from the existing layout engine;
// this module neither allocates slots nor renders controls.
const HEIGHT=1.1547;
const layout=require('./layout');
// New free-space placements need >=85%; retain an existing one down to 84%.
// The neutral band has no-prior fallback at the original floorplan anchor.
const FREE_SCALE=Object.freeze({enter:.85,retain:.84});
const clamp=(n,min,max)=>Math.max(min,Math.min(max,n));
function union(a,b) { return {left:Math.min(a.left,b.left),right:Math.max(a.right,b.right),top:Math.min(a.top,b.top),bottom:Math.max(a.bottom,b.bottom)}; }
function workingFootprint(actual,lastSlot=18) {
    const center=layout.sceneCenter(2),cx=center.x+.5,cy=center.y+HEIGHT/2;
    let result={left:-.5,right:.5,top:-HEIGHT/2,bottom:HEIGHT/2};
    for(let i=0;i<lastSlot;i++) {
        const p=layout.buttonPosition(i,{inner:true,outer:true,radius:2});
        result=union(result,{left:p.x-cx,right:p.x+1-cx,top:p.y-cy,bottom:p.y+HEIGHT-cy});
    }
    return union(result,actual);
}
function footprint(menu) {
    const center=menu._computeCenterPosition(),cx=center.x+.5,cy=center.y+HEIGHT/2;
    const points=[center];
    (menu.buttons || []).forEach((button,i)=>{if(button!==undefined){const p=menu._computeButtonPosition(i);if(p)points.push(p);}});
    // XY controls occupy scene space in addition to their surrounding cubes.
    if(menu.config.xy_pad)points.push({x:0,y:0},{x:menu.sizes.containerWidth/menu.sizes.item-1,y:menu.sizes.containerHeight/menu.sizes.item-HEIGHT});
    return {left:Math.min(...points.map(p=>p.x-cx)),right:Math.max(...points.map(p=>p.x+1-cx)),
        top:Math.min(...points.map(p=>p.y-cy)),bottom:Math.max(...points.map(p=>p.y+HEIGHT-cy))};
}
function boundsAt(f,size,anchor){return {left:anchor.x+f.left*size,right:anchor.x+f.right*size,top:anchor.y+f.top*size,bottom:anchor.y+f.bottom*size};}
function fits(f,size,anchor,region) {
    if(!anchor || !region)return false;
    const b=boundsAt(f,size,anchor),epsilon=.05;
    return b.left>=region.left-epsilon && b.right<=region.right+epsilon && b.top>=region.top-epsilon && b.bottom<=region.bottom+epsilon;
}
function fittedSize(f,region,desired){return Math.max(1,Math.min(desired,(region.right-region.left)/(f.right-f.left),(region.bottom-region.top)/(f.bottom-f.top)));}
function centerIn(f,size,region,preferred=null) {
    return {x:clamp(preferred?preferred.x:(region.left+region.right)/2,region.left-f.left*size,region.right-f.right*size),
        y:clamp(preferred?preferred.y:(region.top+region.bottom)/2,region.top-f.top*size,region.bottom-f.bottom*size)};
}
function freeRegions(viewport,image,gap=12) {
    if(!image)return [];
    if(image.right<=viewport.left || image.left>=viewport.right || image.bottom<=viewport.top || image.top>=viewport.bottom)return [{...viewport,key:'outside'}];
    const regions=[{...viewport,top:Math.max(viewport.top,image.bottom+gap),key:'below'},
        {...viewport,bottom:Math.min(viewport.bottom,image.top-gap),key:'above'},
        {...viewport,right:Math.min(viewport.right,image.left-gap),key:'left'},
        {...viewport,left:Math.max(viewport.left,image.right+gap),key:'right'}];
    return regions.filter(r=>r.right>r.left && r.bottom>r.top);
}
function place(f,viewport,image,desired=100,previous=null,origin=null,planning=workingFootprint(f)) {
    const candidates=freeRegions(viewport,image).map(region=>({region,size:fittedSize(planning,region,desired)}));
    candidates.sort((a,b)=>b.size-a.size || (b.region.right-b.region.left)*(b.region.bottom-b.region.top)-(a.region.right-a.region.left)*(a.region.bottom-a.region.top));
    const reaches=(candidate,threshold)=>candidate.size/desired>=threshold-1e-9;
    let best=candidates.find(c=>reaches(c,FREE_SCALE.enter));
    const retained=previous && previous.region && candidates.find(c=>c.region.key===previous.region.key);
    // Full-size alternatives always beat reduced-size regions. In the neutral
    // band retain a valid prior free-space decision, otherwise prefer the root.
    if(retained && reaches(retained,FREE_SCALE.retain) && (!best ||
        (best.size<desired && (retained.size/desired<FREE_SCALE.enter || retained.size>=best.size-2)) || retained.size===desired))best=retained;
    if(best)return {...centerIn(planning,best.size,best.region,retained===best?previous:null),...best};
    // Do not force the full outer planning ring into the viewport on phones.
    // Reserve center + first ring, unioned with EVERY actual visible control.
    const usable=planning===f?f:workingFootprint(f,6),size=fittedSize(usable,viewport,desired);
    return {...centerIn(usable,size,viewport,origin),region:{...viewport,key:'viewport'},size};
}
function smallScreen(f,viewport,desired=100) {
    // A screen is constrained when the standard working envelope cannot fit at
    // the requested expanded size. Use safe geometry, not a device/width cutoff.
    return fittedSize(workingFootprint(f),viewport,desired)<desired-.001;
}
function placeRoot(f,viewport,image,desired=100,previous=null,origin=null,allowSmallScreen=true) {
    const result=place(f,viewport,image,desired,previous,origin);
    if(!allowSmallScreen || !smallScreen(f,viewport,desired))return result;
    // Preserve the existing size decision. On constrained screens the planning
    // ring must not veto free canvas that fits ALL actually visible controls.
    const candidates=freeRegions(viewport,image)
        .filter(region=>fittedSize(f,region,result.size)>=result.size-.001)
        .map(region=>({...centerIn(f,result.size,region),size:result.size,region}));
    const area=r=>(r.right-r.left)*(r.bottom-r.top);
    const centering=c=>(c.x-(c.region.left+c.region.right)/2)**2+(c.y-(c.region.top+c.region.bottom)/2)**2;
    candidates.sort((a,b)=>Number(b.region.key==='below')-Number(a.region.key==='below') ||
        area(b.region)-area(a.region) || centering(a)-centering(b));
    return candidates[0] || result;
}
function submenu(f,viewport,root,preferred,desired,image=null) {
    const region=root.region && !['viewport','compact'].includes(root.region.key) && fittedSize(f,root.region,desired)>=desired-.001?root.region:viewport;
    if(fits(f,desired,preferred,region))return {...preferred,size:desired,reason:'selected'};
    if(fits(f,desired,root,region))return {x:root.x,y:root.y,size:desired,reason:'root'};
    if(region!==viewport)return {...centerIn(f,desired,region,root),size:desired,reason:'region'};
    // Tiny children use their actual footprint, never the root planning ring.
    const alternate=place(f,viewport,image,desired,root,root,f);
    if(alternate.region.key!=='viewport')return {...alternate,reason:'region'};
    const size=fittedSize(f,viewport,desired);
    return {...centerIn(f,size,viewport,root),size,reason:'viewport'};
}
function chromeElements(owner) {
    const roots=new Set([document]);
    for(let node=owner;node;node=node.parentElement || (node.getRootNode && node.getRootNode().host)){
        const root=node.getRootNode();if(root)roots.add(root);if(node.shadowRoot)roots.add(node.shadowRoot);
    }
    const elements=new Set();
    for(const root of roots)if(root.querySelectorAll)for(const el of root.querySelectorAll('header,footer,#header,#footer,.header,.toolbar,app-header,app-toolbar,ha-top-app-bar-fixed,ha-tabs,ha-sidebar,[data-jts-n-viewport-inset]'))elements.add(el);
    return [...elements].slice(0,64);
}
function environment(menu,owner,image=null) {
    const v=window.visualViewport || {width:innerWidth,height:innerHeight,offsetLeft:0,offsetTop:0};
    const style=getComputedStyle(menu),safe=side=>16+(parseFloat(style.getPropertyValue('--hub-safe-'+side))||0);
    const viewport={left:v.offsetLeft+safe('left'),right:v.offsetLeft+v.width-safe('right'),top:v.offsetTop+safe('top'),bottom:v.offsetTop+v.height-safe('bottom')};
    const chrome=[];
    for(const el of chromeElements(owner)) {
        const css=getComputedStyle(el);
        if(css.display==='none'||css.visibility==='hidden'||!(['fixed','sticky'].includes(css.position)||['app-header','ha-tabs','ha-sidebar'].includes(el.localName)))continue;
        const box=el.getBoundingClientRect();
        if(box.width && box.height && !(box.width>=v.width*.95 && box.height>=v.height*.95))chrome.push(box);
    }
    // Connected header/tab/footer bands may be stacked in either DOM order.
    for(let pass=0;pass<4;pass++) {
        const before=JSON.stringify(viewport);
        for(const b of chrome) {
            if(b.width>=v.width*.5){if(b.top<=viewport.top+1&&b.bottom>viewport.top)viewport.top=Math.min(viewport.bottom-1,b.bottom+16);if(b.bottom>=viewport.bottom-1&&b.top<=viewport.bottom)viewport.bottom=Math.max(viewport.top+1,b.top-16);}
            if(b.height>=v.height*.5){if(b.left<=viewport.left+1&&b.right>viewport.left)viewport.left=Math.min(viewport.right-1,b.right+16);if(b.right>=viewport.right-1&&b.left<viewport.right)viewport.right=Math.max(viewport.left+1,b.left-16);}
        }
        if(JSON.stringify(viewport)===before)break;
    }
    return {viewport,image,key:JSON.stringify([viewport,image])};
}
module.exports={HEIGHT,FREE_SCALE,workingFootprint,footprint,boundsAt,fits,fittedSize,centerIn,freeRegions,smallScreen,placeRoot,place,submenu,chromeElements,environment};
