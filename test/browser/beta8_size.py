"""Configured ceilings and opt-in shared Compass diagnostics. Browser plugin unavailable.
Flow: floorplan -> expanded Hub -> actual module/recursive menus -> exact Back;
normal/expanded Compass inspection -> measured CSS pixels -> resize/cleanup.
All HA data/actions are synthetic.
"""
import argparse,json,os,shutil,threading,unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Handler,CheckResult
from beta5_geometry import Geometry
from dev_build import DevBuild
from charger import charger
from PIL import Image,ImageChops
MATRIX=[('omitted',None,None,82),('auto','auto',None,82),('auto82','auto',82,82),('auto100','auto',100,82),('fixed60',60,None,60),('fixed60_100',60,100,60),('fixed82',82,None,82),('fixed100',100,None,100),('fixed100_70',100,70,70)]

def nested(depth):
 return {'nested_expand':True,'promote_to_center':True,'size':9999,'promoted_center':{'mode':'generic','icon':'jts-n:compass','tap_action':{'action':'jts-n-back'}},'buttons':[{'slot':1,'icon':'mdi:circle','tap_action':{'action':'jts-n-open-nested','jts_n_nested_menu':nested(depth-1)} if depth else {'action':'none'}}]}

class Size(Geometry):
 configured_size=None
 def settle(self):
  self.page.evaluate("""async()=>{await new Promise(requestAnimationFrame);const m=window.hub?._hubMenu;if(m){await m.updateComplete;await Promise.all([...m.shadowRoot.querySelectorAll('jts-n-menu-item,navigation-control')].map(e=>e.updateComplete));await Promise.all(m.shadowRoot.getAnimations({subtree:true}).filter(a=>a.effect?.getComputedTiming().iterations!==Infinity).map(a=>a.finished.catch(()=>{})))}}""")
 def setup_room(self,size=None,expanded=None,debug=None):
  items=[{'type':'light','entity':'light.zone_a','slot':0},{'type':'light','entity':'light.zone_a','slot':2},{**self.sonos_item(),'slot':3},{'type':'climate','entity':'climate.room_a','slot':4},{**charger(1),'slot':5},{'type':'generic','entity':'sensor.value_a','slot':6,'icon':'mdi:circle','tap_action':{'action':'jts-n-open-nested','jts_n_nested_menu':nested(2)}}]
  extra={'collapsible':{'expanded_center':'compass','primary_slot':1,**({'expanded_size':expanded} if expanded is not None else {})},**({'size':size} if size is not None else {}),**({'size_debug':debug} if debug is not None else {})}
  self.floor('above',items=items,policy='compass',extra=extra)
  self.page.evaluate("pushState('light.zone_a','on',{brightness:128,supported_color_modes:['hs','color_temp'],color_mode:'color_temp',min_color_temp_kelvin:2200,max_color_temp_kelvin:6500})");self.settle()
 def widths(self):
  self.settle();return self.controls().evaluate_all("es=>es.map(e=>({width:e.shadowRoot.querySelector('.hex-svg').getBoundingClientRect().width,mode:e.config.mode,entity:e.config.entity}))")
 def check(self,name,limit,policy):
  data=self.widths();self.assertTrue(data)
  for d in data:self.assertLessEqual(d['width'],limit+.15,(name,d,limit));self.assertGreater(d['width'],0)
  self.assertLessEqual(self.page.evaluate('hub._hubMenu.sizes.item'),limit+.0001);self.assert_fit()
  self.measurements.append({'viewport':self.viewport,'policy':policy,'surface':name,'limit':limit,'min':min(d['width'] for d in data),'max':max(d['width'] for d in data),'count':len(data)})
 def same_boxes(self,a,b):
  self.assertEqual(len(a),len(b))
  for x,y in zip(a,b):self.assert_same(x,y)
 def root_back(self,parent):
  while self.page.evaluate('hub._menuContext.stack.length'):
   self.back();self.settle()
  self.same_boxes(parent,self.boxes())
 def test_complete_size_matrix_all_modules(self):
  for policy,size,expanded,limit in MATRIX:
   print('MATRIX',self.viewport,policy,flush=True);self.setup_room(size,expanded,True);collapsed=self.box();self.assertLessEqual(collapsed['width'],82.15 if size in (None,'auto') else size+.15)
   self.page.evaluate("limit=>{window.sizeOvershoots=[];const sample=()=>{if(hub?._hubExpanded)for(const e of hub._hubMenu.shadowRoot.querySelectorAll('jts-n-menu-item,navigation-control')){const width=e.shadowRoot.querySelector('.hex-svg').getBoundingClientRect().width;if(width>limit+.15)sizeOvershoots.push(width)}window.sizeFrame=requestAnimationFrame(sample)};window.sizeFrame=requestAnimationFrame(sample)}",limit)
   self.measurements.append({'viewport':self.viewport,'policy':policy,'surface':'collapsed','limit':82 if size in (None,'auto') else size,'min':collapsed['width'],'max':collapsed['width'],'count':1})
   self.expand();self.page.wait_for_timeout(550);self.check('root-center-ring-Compass',limit,policy);self.assertEqual(self.state()['root']['region']['key'],'below');self.assert_fit(self.state()['root']['region']);root=self.boxes()
   self.cell(2).locator('.interaction-surface').hover();self.check('hover-no-overshoot',limit,policy);self.page.mouse.move(0,0)
   self.hold_input(self.cell(2).locator('.interaction-surface'));self.settle();self.check('Light',limit,policy)
   self.activate(self.cell(3).locator('.interaction-surface'));self.settle();self.check('White-palette',limit,policy);palette=self.boxes();depth=self.page.evaluate('hub._menuContext.stack.length')
   self.hold_input(self.cell(8).locator('.interaction-surface'));self.settle();self.check('Kelvin-zoom',limit,policy);self.assertGreater(self.page.evaluate('hub._menuContext.stack.length'),depth);self.back();self.settle();self.same_boxes(palette,self.boxes())
   self.hold_input(self.cell(3).locator('.interaction-surface'));self.settle();self.check('Color-palette',limit,policy);self.root_back(root)
   self.hold_input(self.cell(3).locator('.interaction-surface'));self.settle();self.check('Sonos',limit,policy);sonos=self.boxes()
   for slot,name in [(1,'Radio'),(3,'Join'),(4,'Sleep')]:
    self.activate(self.cell(slot).locator('.interaction-surface'));self.settle();self.check(name,limit,policy);self.back();self.settle();self.same_boxes(sonos,self.boxes())
   self.root_back(root)
   self.activate(self.cell(4).locator('.interaction-surface'));self.settle();self.check('Climate',limit,policy);self.root_back(root)
   self.hold_input(self.cell(5).locator('.interaction-surface'));self.settle();self.check('Charger',limit,policy);self.root_back(root)
   self.activate(self.cell(6).locator('.interaction-surface'));self.settle();self.check('generic-1',limit,policy);self.cell().locator('.interaction-surface').press('Alt+v');self.page.wait_for_timeout(50);self.assert_debug(self.cell());first=self.boxes()
   self.activate(self.cell(1).locator('.interaction-surface'));self.settle();self.check('recursive-2',limit,policy);second=self.boxes()
   self.activate(self.cell(1).locator('.interaction-surface'));self.settle();self.check('recursive-3',limit,policy)
   self.back();self.settle();self.same_boxes(second,self.boxes());self.back();self.settle();self.same_boxes(first,self.boxes());self.root_back(root);self.check('restored-parent',limit,policy)
   if policy in ('omitted','fixed60','fixed100_70'):
    self.reveal(expanded=True);self.assert_debug(self.cell());self.capture('matrix-'+policy)
   self.page.evaluate('cancelAnimationFrame(sizeFrame)');self.assertEqual(self.page.evaluate('sizeOvershoots'),[])
   self.back();self.settle();self.assert_same(collapsed,self.box());self.assertEqual(self.page.evaluate('calls.length'),0);self.reset()
  (self.evidence/f'{self.viewport["width"]}-size-matrix.json').write_text(json.dumps(self.measurements,indent=2))
 def reveal(self,cell=None,expanded=False):
  cell=cell or self.cell();cell.locator('.interaction-surface').press('Shift+Enter' if expanded else 'Enter');self.page.wait_for_timeout(80);self.settle();return cell
 def assert_debug(self,cell):
  measured=cell.locator('.hex-outer').evaluate('e=>e.getBoundingClientRect().width');label=cell.locator('.compass-size').inner_text();self.assertLessEqual(abs(float(label.split()[0])-measured),.051)
  self.assertIn(label,cell.locator('.compass-version').get_attribute('aria-label'));self.assertTrue(cell.evaluate("e=>{const p=e.shadowRoot.querySelector('.hex-fill'),inv=p.getScreenCTM().inverse();return [...e.shadowRoot.querySelectorAll('.compass-version span')].every(t=>{const r=t.getBoundingClientRect();return [[r.left,r.top],[r.right,r.top],[r.left,r.bottom],[r.right,r.bottom]].every(([x,y])=>p.isPointInFill(new DOMPoint(x,y).matrixTransform(inv)))})}"));return measured
 def test_debug_opt_in_normal_expanded_resize_and_cleanup(self):
  self.page.emulate_media(reduced_motion='reduce')
  paths=[]
  for debug in [None,False,True]:
   self.hub({'size':65,'logo':True,'items':[{'type':'light','entity':'light.zone_a','slot':1}],**({'size_debug':debug} if debug is not None else {})});self.settle();self.assertEqual(self.cell().locator('.compass-size').count(),0)
   if debug:
    self.activate(self.cell().locator('.interaction-surface'));self.page.wait_for_timeout(80);self.settle();cell=self.cell()
   else:cell=self.reveal()
   self.assertIn(DevBuild.expected_label(self),cell.locator('.compass-version').get_attribute('aria-label'))
   if debug:self.assert_debug(cell)
   else:self.assertEqual(cell.locator('.compass-size').count(),0);self.assertIsNone(cell.evaluate('e=>e._compassSizeCleanup'))
   path=self.evidence/f'{self.viewport["width"]}-debug-{debug}.png';cell.screenshot(path=str(path));paths.append(path);self.capture('normal-debug-'+str(debug));self.reset()
  self.assertIsNone(ImageChops.difference(Image.open(paths[0]),Image.open(paths[1])).getbbox())
  for size in [41,60,82,100]:
   self.hub({'size':size,'size_debug':True,'logo':True,'items':[{'type':'light','entity':'light.zone_a','slot':1}]});cell=self.reveal();self.assert_debug(cell)
   cell.evaluate("e=>e.style.transform='scale(.913)'");self.page.wait_for_timeout(100);self.assert_debug(cell);self.capture('measured-transform-'+str(size))
   cell.evaluate("e=>e.style.transform=''");self.page.wait_for_timeout(80);self.assert_debug(cell);self.reset()
  self.setup_room(100,None,True);self.expand();self.page.wait_for_timeout(550);cell=self.cell();self.hold_input(cell.locator('.interaction-surface'));self.settle();self.assert_debug(cell);self.assertTrue(self.page.evaluate('hub._hubExpanded'));self.capture('expanded-debug')
  self.page.set_viewport_size({'width':240,'height':568});self.page.wait_for_timeout(150);self.settle();self.assert_debug(self.cell());self.assertLess(self.box()['width'],100)
  self.capture('live-resized-debug');self.page.evaluate("window.removedCompass=hub._hubMenu.shadowRoot.querySelector('.center-item');hub.remove()");self.page.wait_for_timeout(50);self.assertEqual(self.page.evaluate('[removedCompass._compassSizeFrame,removedCompass._compassSizeCleanup]'),[None,None]);self.assertEqual(self.page.evaluate('calls.length'),0)
 def test_default_ceiling_resize_zoom_and_unavailable(self):
  self.setup_room(None,100,True);self.expand();self.page.wait_for_timeout(550)
  for width,height in [(390,844),(844,390),(800,1280),(1920,1080),(430,932)]:
   self.page.set_viewport_size({'width':width,'height':height});self.page.wait_for_timeout(130);self.settle();self.check('resize-orientation',82,'auto100')
  cdp=self.page.context.new_cdp_session(self.page);cdp.send('Emulation.setPageScaleFactor',{'pageScaleFactor':1.25});self.page.wait_for_timeout(100);self.check('browser-pinch-zoom',82,'auto100');cdp.send('Emulation.setPageScaleFactor',{'pageScaleFactor':1});cdp.detach()
  cell=self.reveal(expanded=True);self.assert_debug(cell);cell.locator('.hex-svg').evaluate("e=>e.style.display='none'");self.page.wait_for_timeout(100);self.assertEqual(cell.locator('.compass-size').inner_text(),'N/A');cell.locator('.hex-svg').evaluate("e=>e.style.display=''");self.page.wait_for_timeout(100);self.assert_debug(cell)
  self.page.wait_for_timeout(3100);self.assertEqual(cell.locator('.compass-size').count(),0);self.assertEqual(cell.evaluate('e=>[e._compassSizeFrame,e._compassSizeCleanup]'),[None,None])
  self.back();self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'))
  errors=self.page.evaluate("()=>[null,0,1,'true',{},[]].map(size_debug=>{try{hub.setConfig({...hub.config,size_debug});return null}catch(e){return e.message}})");self.assertTrue(all(e and 'size_debug' in e for e in errors))
  self.reset();self.viewport={'width':390,'height':844};self.page.set_viewport_size(self.viewport);self.setup_room(100,70,True);self.page.evaluate('hub.setConfig({...hub.config,collapsible:{...hub.config.collapsible,small_screen:false}})');self.settle();self.expand();self.settle();self.check('legacy-compact-opt-out',70,'fixed100_70');self.assertAlmostEqual(self.state()['root']['size'],self.box()['width'],delta=.15);self.back();self.settle();self.assertAlmostEqual(self.box()['width'],100,delta=.15)

 def setUp(self):super().setUp();self.measurements=[]

def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--button-card',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--test-filter');p.add_argument('--quick',action='store_true');a=p.parse_args();a.evidence_dir.mkdir(parents=True,exist_ok=True)
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.bundle=a.bundle.resolve();server.button=a.button_card.resolve();threading.Thread(target=server.serve_forever,daemon=True).start();success=True
 try:
  with sync_playwright() as pw:
   Size.browser=pw.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox']);Size.url=f'http://127.0.0.1:{server.server_port}';Size.evidence=a.evidence_dir
   for width,height in ([(390,844)] if a.quick else [(390,844),(430,932),(800,1280),(1440,900),(1920,1080)]):
    Size.viewport={'width':width,'height':height};names=[n for n in Size.__dict__ if n.startswith('test_') and (not a.test_filter or a.test_filter in n)];r=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(Size(n) for n in names));success=r.wasSuccessful() and success
   Size.browser.close()
 finally:server.shutdown();server.server_close()
 return 0 if success else 1
if __name__=='__main__':raise SystemExit(main())
