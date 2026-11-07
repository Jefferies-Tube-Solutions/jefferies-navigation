import CubeElement from './cube-element.js';

// Menu placement is separate from presentation: native, generic and nested
// controls all consume the shared full-cell engine.
class NavigationMenuItem extends CubeElement {
    static get is() { return 'jts-n-menu-item'; }
}
customElements.define(NavigationMenuItem.is, NavigationMenuItem);
