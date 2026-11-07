const {test}=require('node:test'),assert=require('node:assert/strict');
const g=require('../src/core/expanded-layout');
const {displayedRect}=require('../src/core/image-sizing');
const compass=require('../src/core/compass');
const layout=require('../src/core/layout');
const viewport={left:16,right:374,top:16,bottom:828};
const two={left:-1,right:.5,top:-1.44235,bottom:.57735};
test('asymmetric complete footprint is placed wholly below upper image at comfortable size',()=>{
 const roomy={...viewport,right:784,bottom:1264};const r=g.place(two,roomy,{left:0,right:800,top:0,bottom:390});assert.equal(r.region.key,'below');assert.equal(r.size,100);assert.ok(g.fits(g.workingFootprint(two),r.size,r,r.region));assert.ok(g.boundsAt(two,r.size,r).top>=402);assert.equal(r.x,400);
});
test('all four image-free regions are considered; tiny strips never win over readable fallback',()=>{
 const roomy={left:16,right:1424,top:16,bottom:1064};
 for(const [image,key]of [[{left:0,right:1440,top:600,bottom:1080},'above'],[{left:0,right:500,top:0,bottom:1080},'right'],[{left:940,right:1440,top:0,bottom:1080},'left']]){
  const r=g.place(two,roomy,image);assert.equal(r.region.key,key);assert.ok(g.fits(g.workingFootprint(two),r.size,r,r.region));
 }
 const r=g.place({left:-1.5,right:1.5,top:-1.44,bottom:1.44},viewport,{left:0,right:390,top:0,bottom:800});assert.equal(r.region.key,'viewport');assert.equal(r.size,100);
});
test('actual slot footprint reuses shared center/position coordinates, including extended asymmetric rings',()=>{
 const menu={config:{},_computeCenterPosition:()=>layout.sceneCenter(3),buttons:Array(37),_computeButtonPosition:i=>layout.buttonPosition(i,{inner:true,outer:true,radius:3})};menu.buttons[36]={};
 const f=g.footprint(menu),c=menu._computeCenterPosition(),p=menu._computeButtonPosition(36);assert.ok(f.left<=p.x-c.x-.5);assert.ok(f.right>=p.x-c.x+.5);assert.ok(f.bottom>=p.y-c.y+.57735);assert.ok(f.left<=-.5 && f.right>=.5);
});
test('selected anchor wins by actual fit; constrained child uses root then safe fitting',()=>{
 const f={left:-1.5,right:1.5,top:-1.44,bottom:1.44},root={x:195,y:422};
 assert.equal(g.submenu(f,viewport,root,{x:195,y:200},100).reason,'selected');
 const r=g.submenu(f,viewport,root,{x:300,y:100},100);assert.equal(r.reason,'root');assert.deepEqual([r.x,r.y,r.size],[195,422,100]);
 const large={left:-3,right:3,top:-2,bottom:2};const shrink=g.submenu(large,viewport,root,{x:300,y:100},100);assert.equal(shrink.reason,'viewport');assert.ok(shrink.size<100);assert.ok(g.fits(large,shrink.size,shrink,viewport));
});
test('child preserves a usable image-free region rather than crossing its edge unnecessarily',()=>{
 const f={left:-1.5,right:1.5,top:-1.44,bottom:1.44},root={x:195,y:620,region:{left:16,right:374,top:404,bottom:828,key:'below'}};
 const r=g.submenu(f,viewport,root,{x:195,y:530},100);assert.equal(r.reason,'root');assert.ok(g.fits(f,r.size,r,root.region));
});
test('displayed image rectangle excludes contain letterboxes and clips cover outside its image/card box',()=>{
 const box={left:10,top:20,right:410,bottom:420};assert.deepEqual(displayedRect({x:0,y:100,width:400,height:200},box),{left:10,top:120,right:410,bottom:320});
 assert.deepEqual(displayedRect({x:-200,y:0,width:800,height:400},box,{left:0,top:0,right:300,bottom:500}),{left:10,top:20,right:300,bottom:420});assert.equal(displayedRect(null,box),null);
});
test('stable placement survives tiny viewport changes and keeps a useful previous region',()=>{
 const image={left:100,right:290,top:300,bottom:500},first=g.place(two,viewport,image);const next=g.place(two,{...viewport,right:375},image,100,first);assert.equal(next.region.key,first.region.key);assert.ok(g.fits(two,next.size,next,next.region));
});
test('owner desktop scenarios: full envelope below small image; cramped strip falls back near original cube 0',()=>{
 const v={left:16,right:1424,top:16,bottom:1064},origin={x:650,y:240};
 const a=g.place(two,v,{left:16,right:1424,top:16,bottom:480},100,null,origin);
 assert.equal(a.region.key,'below');assert.equal(a.size,100);assert.ok(g.fits(g.workingFootprint(two),a.size,a,a.region));
 const b=g.place(two,v,{left:16,right:1424,top:16,bottom:850},100,null,origin);
 assert.equal(b.region.key,'viewport');assert.equal(b.size,100);assert.equal(b.x,origin.x);assert.equal(b.y,origin.y);
});
test('100%, 85%, 84% thresholds and neutral-band hysteresis are deterministic in both directions',()=>{
 const v={left:16,right:1424,top:16,bottom:1064},f=g.workingFootprint(two),height=(f.bottom-f.top)*100,origin={x:700,y:200};
 const image=scale=>({left:0,right:1440,top:0,bottom:v.bottom-12-height*scale});
 let prior=null;
 for(const scale of [1,.99,.85,.849,.845,.84,.839,.84,.845,.849,.85,1]) {
  const r=g.place(two,v,image(scale),100,prior,origin);
  const free=scale>=.85 || scale>=.84 && prior?.region.key==='below';
  assert.equal(r.region.key,free?'below':'viewport',String(scale));
  assert.ok(g.fits(free?f:g.workingFootprint(two,6),r.size,r,r.region));
  assert.ok(Math.abs(r.size-(free?scale*100:100))<1e-8);
  if(!free)assert.deepEqual([r.x,r.y],[origin.x,origin.y]);
  prior=r;
 }
 assert.equal(g.place(two,v,image(.845),100,null,origin).region.key,'viewport');
});
test('all alternative regions are evaluated and full size beats a retained reduced region',()=>{
 const v={left:16,right:1424,top:16,bottom:1064},image={left:600,right:1440,top:0,bottom:660};
 const r=g.place(two,v,image,100,{x:900,y:850,region:{key:'below'}});
 assert.equal(r.region.key,'left');assert.equal(r.size,100);
});
test('fallback reserves first ring, clamps minimally at edges, and never discards actual extended controls',()=>{
 const v={left:16,right:374,top:16,bottom:828},origin={x:350,y:50};
 const r=g.place(two,v,null,100,null,origin),usable=g.workingFootprint(two,6);
 assert.equal(r.size,100);assert.ok(g.fits(usable,r.size,r,v));
 assert.deepEqual(r,g.place(two,v,null,100,r,origin));
 assert.deepEqual([r.x,r.y],Object.values(g.centerIn(usable,100,v,origin)));
 const actual={left:-4,right:3,top:-3,bottom:3};const extended=g.place(actual,v,null,100,null,origin);
 assert.ok(g.fits(actual,extended.size,extended,v));assert.ok(extended.size<100);
 assert.ok(Math.abs(extended.size-358/7)<1e-8);
});
test('root planning uses all 19 shared physical coordinates but never creates or mutates buttons',()=>{
 const f=g.workingFootprint(two),center=layout.sceneCenter(2);
 assert.equal(f.right-f.left,5);
 for(let i=0;i<18;i++) { const p=layout.buttonPosition(i,{inner:true,outer:true,radius:2});assert.ok(p.x-center.x-.5>=f.left);assert.ok(p.y-center.y+g.HEIGHT/2<=f.bottom); }
 const beyond={left:-5,right:4,top:-4,bottom:4};assert.deepEqual(g.workingFootprint(beyond),beyond);
});
test('one Compass preset keeps asset, default paint and live build version while contextual action changes',()=>{
 const normal=compass.descriptor(),back=compass.descriptor({}, {collapse:true});assert.deepEqual(normal.colors,back.colors);assert.equal(normal.tap_action.action,'jts-n-compass-inspect');assert.equal(back.tap_action.action,'jts-n-hub-collapse');assert.equal(back.hold_action.action,'jts-n-compass-inspect');assert.equal(compass.asset,require('../src/brand/compass.generated').JTS_N_COMPASS_PNG);assert.equal(typeof compass.version.text,'string');assert.ok(compass.REVEAL_MS>=3000);
 const explicit=compass.descriptor({colors:{center:'#123456'},border:{inner_width:7}});assert.equal(explicit.colors.center,'#123456');assert.equal(explicit.colors.fill_gradient,false);assert.equal(explicit.border.inner_width,7);assert.equal(compass.descriptor({background:'#123456'}).colors.fill_gradient,false);assert.equal(compass.descriptor({styles:{card:[{'background-color':'#123456'}]}}).colors.fill_gradient,false);
});
test('small-screen free canvas fits actual four-cube Hub without shrinking or requiring 19 phantom cubes',()=>{
 const f={left:-1.5,right:1,top:-1.44235,bottom:.57735},image={left:0,right:390,top:0,bottom:330},origin={x:195,y:165};
 const old=g.place(f,viewport,image,100,null,origin),r=g.placeRoot(f,viewport,image,100,null,origin);
 assert.equal(old.region.key,'viewport');assert.ok(g.smallScreen(f,viewport,100));
 assert.equal(r.region.key,'below');assert.equal(r.size,old.size);assert.equal(r.x,195);
 assert.ok(g.fits(f,r.size,r,r.region));assert.ok(g.boundsAt(f,r.size,r).top>=342);
});
test('small-screen detection uses usable working-envelope geometry, not a phone CSS-width boundary',()=>{
 const f={left:-.5,right:.5,top:-g.HEIGHT/2,bottom:g.HEIGHT/2};
 assert.equal(g.smallScreen(f,{left:16,right:828,top:16,bottom:374},100),true);
 assert.equal(g.smallScreen(f,{left:16,right:784,top:16,bottom:1264},100),false);
 assert.equal(g.smallScreen(f,viewport,50),false);
});
test('mobile prefers a fitting lower region even when another is larger; other zones use space and centering',()=>{
 const f={left:-1,right:.5,top:-.6,bottom:.6},v={left:16,right:374,top:16,bottom:828};
 const r=g.placeRoot(f,v,{left:0,right:390,top:450,bottom:650},100);
 assert.equal(r.region.key,'below');assert.equal(r.size,100);assert.ok(g.fits(f,r.size,r,r.region));
 const other=g.placeRoot(f,v,{left:200,right:390,top:400,bottom:844},100);
 assert.equal(other.region.key,'left');assert.ok(g.fits(f,other.size,other,other.region));
});
test('mobile cannot discard extended controls or further shrink just to occupy a free strip',()=>{
 const f={left:-3,right:3,top:-2,bottom:2},image={left:0,right:390,top:0,bottom:750},origin={x:195,y:375};
 const old=g.place(f,viewport,image,100,null,origin),r=g.placeRoot(f,viewport,image,100,null,origin);
 assert.deepEqual(r,old);assert.ok(g.fits(f,r.size,r,viewport));
 assert.deepEqual(g.placeRoot(two,viewport,null,100,null,origin),g.place(two,viewport,null,100,null,origin));
});
test('desktop results and explicit small-screen opt-out preserve beta.6 scaling, anchor and thresholds exactly',()=>{
 const v={left:16,right:1424,top:16,bottom:1064},origin={x:720,y:440};
 for(const bottom of [480,672,676,680,880]) {
  const image={left:0,right:1440,top:0,bottom};const old=g.place(two,v,image,100,null,origin);
  assert.deepEqual(g.placeRoot(two,v,image,100,null,origin),old);
 }
 const image={left:0,right:390,top:0,bottom:330};
 assert.deepEqual(g.placeRoot(two,viewport,image,100,null,origin,false),g.place(two,viewport,image,100,null,origin));
});
