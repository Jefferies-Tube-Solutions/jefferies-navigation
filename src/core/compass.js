// The same compass and paint are used on every navigation surface.
const merge=require('lodash/merge');
const {JTS_N_COMPASS_PNG}=require('../brand/compass.generated');
const {versionLabel}=require('./version-label');
const {OUTER}=require('./submenu-theme');
const COLORS=Object.freeze({center:'#101e34',inner_border:'#38516c',outer_border:OUTER,unavailable:'#20262d'});
const version=versionLabel(require('./build-info').version);
const CALIBRATION_MS=430,REVEAL_MS=3000,ICON_PERCENT=58,VERSION_ICON_PERCENT=34;
function isCompass(config){return !!config && (config.icon==='jts-n:compass' || config.icon==='');}
function isBrand(config){return isCompass(config) && (config.mode==='hub' || config._decorative_logo===true);}
function descriptor(overrides={},options={}) {
    const colors={...COLORS,...overrides.colors};
    for(const key of ['center','inner_border','outer_border'])if(!colors[key]||colors[key]==='auto')colors[key]=COLORS[key];
    const explicit=options.explicitCenter!==undefined?options.explicitCenter:!!(overrides.colors && overrides.colors.center && overrides.colors.center!=='auto');
    const background=overrides.background!==undefined || ((overrides.styles || {}).card || []).some(rule=>['background','background-color','backgroundColor'].some(key=>Object.prototype.hasOwnProperty.call(rule,key)));
    if(colors.fill_gradient===undefined)colors.fill_gradient=explicit || background?false:{type:'radial'};
    return merge({mode:'hub',icon:'jts-n:compass',_decorative_logo:true,interactive:true,autoclose:false,
        show_name:false,show_label:false,show_brightness:'never',show_volume:'never',face_mode:'cell',
        tap_action:{action:'jts-n-compass-inspect'},hold_action:{action:'jts-n-compass-inspect'}},overrides,{colors,_compass_explicit_center:explicit},
        options.collapse?{tap_action:{action:'jts-n-hub-collapse'},hold_action:{action:'jts-n-compass-inspect'}}:{});
}
function accessible(config,fallback) {
    if(!isBrand(config))return (fallback || config.name || config.entity || 'Jefferies Navigation')+'. Alt+V inspects installed Jefferies Navigation version.';
    const back=config.tap_action && config.tap_action.action==='jts-n-hub-collapse';
    return back?'Back / Collapse Hub. Hold or Shift+Enter to inspect installed Jefferies Navigation version.':'Jefferies Navigation Compass. Inspect installed version; hold or Shift+Enter.';
}
function versionFont(){return Math.min(.12,.57/(Math.max(version.base.length,version.stage.length)*.65));}
function pixelLabel(width) {
    return Number.isFinite(width) && width>0 ? `${Math.round(width*10)/10} px` : 'N/A';
}
module.exports={pixelLabel,COLORS,asset:JTS_N_COMPASS_PNG,version,CALIBRATION_MS,REVEAL_MS,ICON_PERCENT,VERSION_ICON_PERCENT,isCompass,isBrand,descriptor,accessible,versionFont};
