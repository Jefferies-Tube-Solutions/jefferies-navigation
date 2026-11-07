const {allocateHubSlots,MAX_HUB_SLOT}=require('./hub-allocation');
const {numericSize}=require('./image-sizing');
function sizeCeiling(size) { return numericSize(size); }
function settings(value,hubSize) {
    if(value===undefined || value===false)return null;
    const config=value===true?{}:value;
    if(!config || typeof config!=='object' || Array.isArray(config))throw Error('collapsible must be true, false or an options object.');
    for(const key of Object.keys(config))if(!['expanded_center','primary_slot','idle_timeout','mobile','small_screen','expanded_size','beam_of_origin'].includes(key))throw Error('Unknown collapsible option: '+key);
    if(config.mobile!==undefined && config.small_screen!==undefined && config.mobile!==config.small_screen)throw Error('Conflicting collapsible.mobile and collapsible.small_screen; remove mobile or use matching values.');
    const ceiling=sizeCeiling(hubSize);
    const result={expanded_center:'primary',idle_timeout:30000,expanded_size:ceiling,...config,small_screen:config.small_screen!==undefined?config.small_screen:config.mobile!==undefined?config.mobile:true};
    delete result.mobile;
    result.beam_of_origin=require('./beam-of-origin').settings(config.beam_of_origin);
    if(!['primary','compass'].includes(result.expanded_center))throw Error('collapsible.expanded_center must be primary or compass.');
    if(result.expanded_center==='compass' && (!Number.isSafeInteger(result.primary_slot)||result.primary_slot<1||result.primary_slot>MAX_HUB_SLOT))throw Error('collapsible.primary_slot must be an available slot 1–216 for compass center.');
    if(!Number.isFinite(result.idle_timeout)||result.idle_timeout<1000)throw Error('collapsible.idle_timeout must be at least 1000 milliseconds.');
    if(typeof result.small_screen!=='boolean' || config.mobile!==undefined && typeof config.mobile!=='boolean'||config.expanded_size!==undefined && (!Number.isFinite(config.expanded_size)||config.expanded_size<44||config.expanded_size>200))throw Error('Invalid collapsible small_screen/mobile/expanded_size option.');
    result.expanded_size=Math.min(result.expanded_size,ceiling);
    return result;
}
function expandedAllocation(entries,primary,options,previous=new Map()) {
    const moved=options.expanded_center==='compass';
    const expanded=entries.map(entry=>entry.id===primary.id && moved?{...entry,slot:options.primary_slot,mode:'hard'}:entry);
    const result=allocateHubSlots(expanded,{previous,centerReserved:moved});
    if(result.diagnostics.some(d=>['hard-collision','invalid-slot','overflow'].includes(d.code)))throw Error('collapsible expanded slot conflict: '+JSON.stringify(result.diagnostics));
    return result;
}
// Compatibility adapter for the former container-based helper. Active expanded
// scenes use the actual visible footprint and the same shared placement solver.
function mobileGeometry(menu,viewport,desired=100,safe={}) {
    const geometry=require('./expanded-layout'),w=menu.sizes.containerWidth/menu.sizes.item,h=menu.sizes.containerHeight/menu.sizes.item;
    return geometry.place({left:-w/2,right:w/2,top:-h/2,bottom:h/2},
        {left:viewport.offsetLeft+16+(safe.left||0),right:viewport.offsetLeft+viewport.width-16-(safe.right||0),
        top:viewport.offsetTop+16+(safe.top||0),bottom:viewport.offsetTop+viewport.height-16-(safe.bottom||0)},null,desired);
}
module.exports={sizeCeiling,settings,expandedAllocation,mobileGeometry};
