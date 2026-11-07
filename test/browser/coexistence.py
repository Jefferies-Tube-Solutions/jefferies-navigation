"""Full upstream/JTS-N bundle coexistence; real Chromium, synthetic HA, no live HA.
Browser plugin not available. Upstream immutable bundle and digest are pinned.
"""
import argparse,hashlib,importlib.util,os,shutil,threading
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Handler,ROOT,BUTTON_SHA
UPSTREAM_SHA='dc72dfe01fef91eb720c464eae7374c71c3739773c7503492a30f1f0c7c0c35c'
class MixedHandler(Handler):
    def do_GET(self):
        if self.path in ('/','/original.js'):
            self.send_response(200);self.send_header('Content-Type','text/html' if self.path=='/' else 'text/javascript');self.end_headers()
            data=(ROOT/'test/browser/fixture.html').read_text().replace("await import('/bundle.js');",'') if self.path=='/' else self.server.original.read_text()
            self.wfile.write(data.encode());return
        super().do_GET()
def main():
    a=argparse.ArgumentParser();a.add_argument('--bundle',type=Path,required=True);a.add_argument('--original',type=Path,required=True);a.add_argument('--button-card',type=Path,required=True);a.add_argument('--evidence-dir',type=Path,required=True);args=a.parse_args()
    assert hashlib.sha256(args.original.read_bytes()).hexdigest()==UPSTREAM_SHA
    assert hashlib.sha256(args.button_card.read_bytes()).hexdigest()==BUTTON_SHA
    args.evidence_dir.mkdir(parents=True,exist_ok=True)
    server=ThreadingHTTPServer(('127.0.0.1',0),MixedHandler);server.bundle=args.bundle.resolve();server.button=args.button_card.resolve();server.original=args.original.resolve()
    threading.Thread(target=server.serve_forever,daemon=True).start();count=0
    try:
        with sync_playwright() as pw:
            b=pw.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox'])
            for width,height in [(1100,900),(390,844)]:
                for order in [('original',),('ng',),('original','ng'),('ng','original')]:
                    page=b.new_page(viewport={'width':width,'height':height},has_touch=width<500);errors=[]
                    page.on('pageerror',lambda e:errors.append(str(e)));page.on('console',lambda e:errors.append(e.text) if e.type=='error' else None)
                    page.goto(f'http://127.0.0.1:{server.server_port}');page.wait_for_function('window.ready')
                    assert page.title()=='Jefferies Navigation shared cube test' and page.locator('h1').is_visible()
                    for plugin in order:
                        page.add_script_tag(url='/original.js' if plugin=='original' else '/bundle.js')
                        if plugin=='original':page.evaluate('window.originalAPI=window.honeycomb_menu;window.originalItem=customElements.get("honeycomb-menu-item");window.originalTemplates={station:"upstream"};window.honeycomb_menu_templates=originalTemplates')
                        else:page.evaluate('window.ngAPI=window.jefferiesNavigation;window.ngElement=customElements.get("jts-n-menu");window.ngTemplates={};jefferiesNavigation.templates=ngTemplates')
                    if 'original' in order:
                        assert page.evaluate('window.honeycomb_menu===originalAPI && customElements.get("honeycomb-menu-item")===originalItem && window.honeycomb_menu_templates===originalTemplates')
                        page.evaluate("honeycomb_menu({entity:'light.zone_a',buttons:[{icon:'mdi:lightbulb',tap_action:{action:'more-info'}}]})")
                        page.locator('honeycomb-menu honeycomb-menu-item').first.wait_for()
                    if 'ng' in order:
                        assert page.evaluate('window.jefferiesNavigation===ngAPI && jefferiesNavigation.apiVersion===2 && jefferiesNavigation.templates===ngTemplates && customElements.get("jts-n-menu")===ngElement')
                        assert page.evaluate('''() => ['navigation-hub','navigation-control'].every(type =>
                            customElements.get(type) && window.customCards.filter(card => card.type === type).length === 1)''')
                        assert page.evaluate('!customElements.get("jts-n-hub") && !customElements.get("jts-n-control")')
                        page.evaluate("jefferiesNavigation.open({entity:'light.zone_a',animate:false,buttons:[{icon:'mdi:lightbulb',tap_action:{action:'more-info'}}]})")
                        page.locator('jts-n-menu jts-n-menu-item').first.wait_for()
                        target=page.locator('jts-n-menu jts-n-menu-item .interaction-surface').first
                        target.tap() if width<500 else target.click()
                        page.wait_for_function("moreInfo.includes('light.zone_a')")
                        page.evaluate('jefferiesNavigation.close()');page.wait_for_function('!view.querySelector("jts-n-menu")')
                        page.evaluate("jefferiesNavigation.open({entity:'light.zone_a',animate:false,xy_pad:{on_release:true,x:{service:'light.turn_on',data:{entity_id:'entity',brightness:'{{x}}'}}},buttons:[{icon:'mdi:lightbulb'}]})")
                        page.locator('jts-n-menu jts-n-xy-pad').wait_for()
                        page.evaluate("view.querySelector('jts-n-menu').shadowRoot.querySelector('jts-n-xy-pad').dispatchEvent(new CustomEvent('jts-n-drag-end',{detail:{x:123,y:0}}))")
                        page.wait_for_function("calls.some(c=>c[0]==='light' && c[1]==='turn_on' && Number(c[2].brightness)===123)")
                        page.evaluate('jefferiesNavigation.close()');page.wait_for_function('!view.querySelector("jts-n-menu")')
                        if 'original' in order:assert page.locator('honeycomb-menu').count()==1
                        # Explicit JTS-N event never triggers original, regardless of load order.
                        page.evaluate("document.body.dispatchEvent(new CustomEvent('ll-custom',{detail:{jts_n_menu:{entity:'light.zone_a',animate:false,buttons:[{icon:'mdi:lightbulb'}]}},bubbles:true}))")
                        page.locator('jts-n-menu').wait_for()
                        if 'original' in order:assert page.locator('honeycomb-menu').count()==1
                        page.evaluate('jefferiesNavigation.close()');page.wait_for_function('!view.querySelector("jts-n-menu")')
                        # The original key is handled exclusively by the upstream runtime.
                        page.evaluate("document.body.dispatchEvent(new CustomEvent('ll-custom',{detail:{honeycomb_menu:{entity:'light.zone_a',animate:false,buttons:[{icon:'mdi:lightbulb'}]}},bubbles:true}))")
                        assert page.locator('jts-n-menu').count()==0
                        page.evaluate("makeHub({logo:false,items:[{type:'light',entity:'light.zone_a'}]})")
                        page.locator('jts-n-menu .center-item').wait_for()
                        page.evaluate('jefferiesNavigation.disposeContext(hub._menuContext);hub.remove()')
                        page.evaluate("makeControl({module:'sonos',entity:'media_player.player_a'})")
                        target=page.locator('#anchor .interaction-surface');target.wait_for()
                        page.evaluate('control._openMenu()')
                        page.locator('jts-n-menu').wait_for()
                        page.evaluate('jefferiesNavigation.close()')
                    else:assert page.evaluate('window.jefferiesNavigation===undefined && !customElements.get("jts-n-menu")')
                    assert not page.locator('hui-error-card').count()
                    page.screenshot(path=str(args.evidence_dir/f'{width}-{"-".join(order)}.png'),full_page=True)
                    assert errors==[],errors;page.close();count+=1;print(f'PASS {width} {order}',flush=True)
            b.close()
    finally:server.shutdown();server.server_close()
    print(f'{count} full-bundle desktop/mobile coexistence scenarios passed')
if __name__=='__main__':main()
