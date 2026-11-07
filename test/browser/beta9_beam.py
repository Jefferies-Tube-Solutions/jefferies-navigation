"""Beam of Origin: synthetic HA, shared live inert source and measured hex caps.
Browser plugin unavailable; repository Playwright/system Chromium fallback.
"""
import argparse,json,os,shutil,threading,unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Handler,CheckResult
from beta5_geometry import Geometry
from charger import charger

class Beam(Geometry):
 configured_size=None
 def controls(self):return self.page.locator('jts-n-menu #navigation-cells > :is(jts-n-menu-item,navigation-control)')
 def origin(self):return self.page.locator('jts-n-menu .origin-reference')
 def scene(self):return self.page.locator('jts-n-menu .origin-scene')
 def room(self,region='above',extra=None,items=None):
  self.floor(region,items=items,extra={'collapsible':{'beam_of_origin':True},**(extra or {})})
  self.source=self.cell().locator('.hex-svg').bounding_box()
 def linked(self):
  try:self.page.wait_for_function('hub._originGeometry && !hub._hubMenu.shadowRoot.querySelector(".origin-scene").hidden')
  except Exception:
   print('LINK FAILURE',self.page.evaluate('()=>({expanded:hub._hubExpanded,reference:hub._originReference,geometry:hub._originGeometry,source:hub.getBoundingClientRect().toJSON(),root:hub._expandedRoot,stack:hub._menuContext.stack.length,scene:hub._hubMenu.shadowRoot.querySelector(".origin-scene")?.outerHTML})'),flush=True);raise
  self.settle();g=self.page.evaluate('hub._originGeometry');b=self.origin().locator('.hex-svg').bounding_box()
  for key in ['x','y','width','height']:self.assertAlmostEqual(b[key],self.source[key],delta=.25)
  self.assertEqual(self.origin().locator('.interaction-surface').count(),0)
  self.assertTrue(self.origin().evaluate('e=>e.inert && e.visualOnly && !e._moduleObserver && !e._hasHassProvider && !e._imageSizingCleanup'))
  self.assertEqual(self.scene().get_attribute('aria-hidden'),'true')
  self.assertEqual(self.scene().evaluate('e=>getComputedStyle(e).pointerEvents'),'none')
  self.assertGreater(len(g['points']),3)
  # The beam stays behind cubes and above the outside-click shield; neither it
  # nor the inert reference can intercept focus or pointer targeting.
  self.assertLess(int(self.scene().evaluate('e=>getComputedStyle(e).zIndex')),0)
  self.assertEqual(self.scene().locator('[tabindex="0"]').count(),0)
  self.assertEqual(self.page.locator('.hub-shield').evaluate('e=>getComputedStyle(e).zIndex'),'-2')
  return g
 def test_off_default_custom_color_live_source_and_safe_actions(self):
  self.floor('above',extra={'collapsible':True});self.expand();self.assertEqual(self.scene().count(),0);self.back();self.settle();self.reset()
  for options in [True,{'color':'#ffa75a'}]:
   self.room(extra={'size':60,'collapsible':{'beam_of_origin':options},'colors':{'inner_border':'#42ca87'}})
   initial=self.cell().evaluate('e=>({model:e._model,border:e._visualBorder})');self.expand();self.linked()
   self.assertEqual(self.origin().evaluate('e=>e._model'),initial['model']);self.assertEqual(self.origin().evaluate('e=>e._visualBorder'),initial['border'])
   self.assertEqual(self.page.locator('.origin-beam stop').first.get_attribute('stop-color'),options['color'] if isinstance(options,dict) else '#8bdcff')
   self.assertEqual(self.page.locator('.origin-beam stop').first.get_attribute('stop-opacity'),'.34');self.assertEqual(self.page.locator('.origin-beam stop').last.get_attribute('stop-opacity'),'.025')
   self.page.evaluate("pushState('light.zone_a','on',{...hass.states['light.zone_a'].attributes,brightness:77,friendly_name:'Room reference',rgb_color:[12,150,220]})");self.settle()
   self.assertEqual(self.origin().evaluate('e=>e._model.secondary'),self.cell().evaluate('e=>e._model.secondary'))
   self.page.evaluate("pushState('light.zone_a','off',{...hass.states['light.zone_a'].attributes})");self.settle();self.assertEqual(self.origin().evaluate('e=>e._model.colors'),self.cell().evaluate('e=>e._model.colors'))
   self.capture('live-origin-custom' if isinstance(options,dict) else 'live-origin-default')
   self.origin().evaluate("e=>{e._executeAction({action:'toggle'});e._dispatchAction({action:'toggle'});e.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));e.dispatchEvent(new PointerEvent('pointerdown',{bubbles:true}))}")
   self.assertEqual(self.page.evaluate('calls.length'),0)
   self.assertTrue(self.page.evaluate('()=>{ng.backInContext(hub._menuContext);return !hub._hubMenu.shadowRoot.querySelector(".origin-scene") && !hub._originFrame && !hub._originAnimationEnd}'));self.settle();self.assertEqual(self.scene().count(),0);self.assert_same(self.source,self.cell().locator('.hex-svg').bounding_box());self.assertEqual(self.controls().count(),1)
   self.activate(self.cell().locator('.interaction-surface'));self.assertEqual(self.page.evaluate('calls.length'),1);self.reset()
 def test_all_directions_actual_geometry_overlap_and_source_hidden(self):
  self.room(extra={'size':60});self.expand();self.linked()
  for dx,dy in [(230,0),(-230,0),(0,240),(0,-240),(200,220),(-200,-220)]:
   self.page.evaluate('([dx,dy])=>{const r=hub.getBoundingClientRect();hub._hubMenu.reanchor(r.left+r.width/2+dx,r.top+r.height/2+dy);hub._scheduleOriginGeometry()}',[dx,dy]);self.page.wait_for_timeout(50);self.linked()
  self.page.evaluate('()=>{const r=hub.getBoundingClientRect();hub._hubMenu.reanchor(r.left+r.width/2,r.top+r.height/2);hub._scheduleOriginGeometry()}');self.page.wait_for_timeout(50)
  self.assertTrue(self.scene().evaluate('e=>e.hidden'));self.assertEqual(self.controls().count(),2)
  self.page.evaluate("hub.style.left='-1000px'");self.page.wait_for_timeout(100);self.assertTrue(self.scene().evaluate('e=>e.hidden'))
  self.back();self.settle();self.assertEqual(self.scene().count(),0)
 def test_module_navigation_promotion_Back_and_Info_priority(self):
  cases=[('Light',{'type':'light','entity':'light.zone_a'},True),('Sonos',self.sonos_item(),True),('Climate',{'type':'climate','entity':'climate.room_a'},False),('Charger',charger(1),True),('Generic',{'type':'generic','entity':'sensor.value_a','icon':'mdi:circle','tap_action':{'action':'jts-n-open-nested','jts_n_nested_menu':{'nested_expand':True,'promote_to_center':True,'promoted_center':{'mode':'generic','icon':'mdi:circle'},'buttons':[{'slot':1,'icon':'mdi:circle','tap_action':{'action':'none'}}]}}},False)]
  for name,item,hold in cases:
   self.room(items=[{'type':'light','entity':'light.zone_a','slot':0},{**item,'slot':3}]);self.expand();self.page.wait_for_timeout(550);root=self.linked();self.capture('root-'+name)
   if hold:self.hold_input(self.cell(3).locator('.interaction-surface'))
   else:self.activate(self.cell(3).locator('.interaction-surface'))
   self.settle();self.linked();self.assertGreater(self.page.evaluate('hub._menuContext.stack.length'),0);self.assert_fit();self.capture('submenu-'+name)
   if name=='Sonos':
    self.activate(self.sonos_slot(1).locator('.interaction-surface'));self.settle();self.linked();self.capture('Radio');self.back();self.settle()
   if name=='Light':
    self.activate(self.cell(3).locator('.interaction-surface'));self.settle();self.linked();self.capture('Light-palette');self.back();self.settle()
   self.page.evaluate("ng.openInfoInContext(hub._menuContext,{title:'Read only',text:'Synthetic Info'})");self.settle();self.assertTrue(self.page.locator('jts-n-info-cube').evaluate("e=>e.matches(':popover-open')"));self.assertTrue(self.scene().is_visible());self.page.locator('jts-n-info-cube .surface').press('Escape');self.settle();self.linked()
   self.back();self.settle();restored=self.linked();self.assertEqual(root['target'],restored['target']);self.assertEqual(self.page.evaluate('calls.length'),0);self.back();self.settle();self.assertEqual(self.scene().count(),0);self.reset()
 def test_resize_scroll_zoom_reconfigure_multiple_Hubs_and_cleanup(self):
  self.room(extra={'size':'auto','size_debug':True});self.expand();self.linked();self.capture('floorplan-linked')
  self.page.evaluate("window.other=addOverlay({size:60,collapsible:{beam_of_origin:true},items:[{type:'light',entity:'light.zone_b',slot:0},{type:'light',entity:'light.zone_a',slot:2}]},'70%','30%')");self.page.wait_for_function('other._hubMenu?.isConnected');self.page.evaluate('other._expandHub()');self.settle()
  ids=self.page.locator('.origin-beam linearGradient').evaluate_all('es=>es.map(e=>e.id)');self.assertEqual(len(ids),2);self.assertEqual(len(set(ids)),2)
  self.page.evaluate('other.remove()');self.settle();self.assertEqual(self.page.locator('.origin-beam').count(),1)
  self.page.evaluate("floor.style.top='90px';document.dispatchEvent(new Event('scroll'))");self.page.wait_for_timeout(100)
  self.source=self.page.evaluate('()=>{const r=hub._originGeometry.sourceRect;return {x:r.left,y:r.top,width:r.width,height:r.height}}');self.linked()
  self.page.evaluate("document.body.style.zoom='0.9'");self.page.wait_for_timeout(120);self.settle();self.assertTrue(self.page.evaluate('!hub._originFrame'));self.page.evaluate("document.body.style.zoom=''")
  self.page.set_viewport_size({'width':self.viewport['height'],'height':self.viewport['width']});self.page.wait_for_timeout(120);self.settle();self.assert_fit()
  self.page.evaluate('hub.setConfig({...hub.config,collapsible:true})');self.settle();self.assertEqual(self.scene().count(),0);self.assertFalse(self.page.evaluate('hub._hubExpanded'))
  self.page.evaluate('hub.setConfig({...hub.config,collapsible:{beam_of_origin:true}})');self.settle();self.expand();self.page.evaluate('window.removed=hub;hub.remove()');self.settle();self.assertEqual(self.scene().count(),0)
  self.assertTrue(self.page.evaluate('!removed._originReference && !removed._originFrame && !removed._anchorCleanup && removed._expansionChromeResize && !removed._hubMenu'))
 def test_side_regions_cropping_zoom_and_size_ceiling(self):
  for size,limit in [('auto',82),(60,60),(82,82),(100,100)]:
   self.room('left' if self.viewport['width']>800 else 'above',extra={'size':size,'size_debug':True,'collapsible':{'beam_of_origin':True,'expanded_center':'compass','primary_slot':1}})
   self.page.evaluate("pushState('light.zone_a','on',{...hass.states['light.zone_a'].attributes,brightness:190})")
   self.expand();self.linked();self.assertLessEqual(self.box()['width'],limit+.2)
   if self.viewport['width']>800:self.assertEqual(self.state()['root']['region']['key'],'right')
   self.cell().locator('.interaction-surface').press('Shift+Enter');self.page.wait_for_timeout(70)
   self.assertIn('px',self.cell().locator('.compass-size').inner_text());self.capture('side-origin-size-'+str(size))
   # Explicit object-fit crop/object-position must not move the reference to the image's center.
   self.page.evaluate("floorImage.style.objectFit='cover';floorImage.style.objectPosition='right bottom'");self.page.wait_for_timeout(120);self.settle()
   cropped=self.origin().locator('.hex-svg').bounding_box()
   if cropped:
    self.back();self.settle();self.assert_same(cropped,self.cell().locator('.hex-svg').bounding_box())
   else:
    self.assertTrue(self.scene().evaluate('e=>e.hidden'));self.back();self.settle()
   self.page.evaluate("floorImage.style.objectPosition='50% 50%'");self.page.wait_for_timeout(120);self.settle()
   self.source=self.cell().locator('.hex-svg').bounding_box();self.expand();self.linked()
   # CSS zoom is in addition to the runner's viewport/physical pixel geometry.
   ratio=self.page.evaluate('hub._originReference.scale')
   self.page.evaluate("document.body.style.zoom='0.9'");self.page.wait_for_timeout(130);self.settle()
   self.source=self.page.evaluate('r=>{const a=hub.getBoundingClientRect(),w=a.width*r,h=w*hub._originReference.ratio;return {x:a.left+a.width/2-w/2,y:a.top+a.height/2-h/2,width:w,height:h}}',ratio)
   self.linked();self.capture('zoomed-origin-'+str(size));self.page.evaluate("document.body.style.zoom=''");self.page.wait_for_timeout(100)
   self.back();self.settle();self.assertEqual(self.scene().count(),0);self.assertIsNone(self.page.evaluate('hub._originAnimationEnd'));self.assertEqual(self.page.evaluate('calls.length'),0);self.reset()

 def test_reference_right_source_and_cluster_silhouette(self):
  self.room('right' if self.viewport['width']>800 else 'above',items=[{'type':'light','entity':'light.zone_a','slot':0},{**self.sonos_item(),'slot':2},{'type':'light','entity':'light.zone_a','slot':3}],extra={'collapsible':{'beam_of_origin':True,'expanded_center':'compass','primary_slot':1}})
  self.page.evaluate("pushState('light.zone_a','on',{...hass.states['light.zone_a'].attributes,brightness:204})")
  self.expand();self.linked();self.assert_fit()
  if self.viewport['width']>800:self.assertEqual(self.state()['root']['region']['key'],'left')
  self.capture('reference-source-right-cluster-left' if self.viewport['width']>800 else 'reference-source-above-cluster-below')
  self.back();self.settle();self.assertEqual(self.scene().count(),0);self.assertEqual(self.page.evaluate('calls.length'),0)

 def test_Escape_timeout_outside_and_fallback_cleanup(self):
  self.page.clock.install();self.room(extra={'collapsible':{'beam_of_origin':True,'idle_timeout':1000}});self.expand();self.page.clock.run_for(50);self.linked();self.page.clock.run_for(1100);self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertEqual(self.scene().count(),0)
  self.expand();self.page.clock.run_for(550);self.page.keyboard.press('Escape');self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertEqual(self.scene().count(),0)
  self.expand();self.page.clock.run_for(550);self.page.mouse.click(2,2);self.settle();self.assertFalse(self.page.evaluate('hub._hubExpanded'));self.assertEqual(self.scene().count(),0);self.assertEqual(self.page.evaluate('calls.length'),0)
  self.reset();self.room('full');self.expand();self.settle();self.assertEqual(self.state()['root']['region']['key'],'viewport');self.assertTrue(self.scene().evaluate('e=>e.hidden'));self.assertEqual(self.controls().count(),2);self.capture('overlap-fallback-no-duplicate')

# Only this feature's tests, not inherited suites (those run separately in CI).
def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--button-card',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--test-filter');a=p.parse_args();a.evidence_dir.mkdir(parents=True,exist_ok=True)
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.bundle=a.bundle.resolve();server.button=a.button_card.resolve();threading.Thread(target=server.serve_forever,daemon=True).start();ok=True
 try:
  with sync_playwright() as runtime:
   Beam.browser=runtime.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox']);Beam.url=f'http://127.0.0.1:{server.server_port}'
   for width,height in [(390,844),(1440,900)]:
    Beam.viewport={'width':width,'height':height};Beam.evidence=a.evidence_dir;names=[n for n in Beam.__dict__ if n.startswith('test_') and (not a.test_filter or a.test_filter in n)]
    result=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(Beam(n) for n in names));ok=result.wasSuccessful() and ok
   Beam.browser.close()
 finally:server.shutdown()
 return 0 if ok else 1
if __name__=='__main__':raise SystemExit(main())
