import CubeElement from './cube-element.js';

// The standalone adapter resolves the same modules and uses the same renderer
// as Hub items and nested menu cubes. Public mode aliases remain optional.
class NavigationControl extends CubeElement {
    static get is() { return 'navigation-control'; }
}
if (!customElements.get(NavigationControl.is))
    customElements.define(NavigationControl.is, NavigationControl);
window.customCards = window.customCards || [];
if (!window.customCards.some(card=>card.type===NavigationControl.is))
    window.customCards.push({type:NavigationControl.is,name:'Jefferies Navigation Persistent Control',
        description:'Single module using the shared Jefferies Navigation cube engine.'});
export default NavigationControl;
