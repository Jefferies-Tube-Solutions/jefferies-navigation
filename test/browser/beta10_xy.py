"""#154 B1: actual XY events, cancellation, detached-scene action guards and cleanup.
Synthetic HA only. Browser plugin not available; repository Playwright/Chromium.
"""
import argparse,json,os,shutil,threading,unittest
from pathlib import Path
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from run import Cubes,Handler,CheckResult

TRACK=r'''(()=>{
 const add=EventTarget.prototype.addEventListener,remove=EventTarget.prototype.removeEventListener,entries=new Map();
 const track=t=>t===document||t===window;
 const key=(target,type,o)=>(target===document?'document':'window')+':'+type+':'+(typeof o==='boolean'?o:!!o?.capture);
 EventTarget.prototype.addEventListener=function(type,fn,o){if(track(this)){const k=key(this,type,o);if(!entries.has(k))entries.set(k,new Set());entries.get(k).add(fn)}return add.call(this,type,fn,o)};
 EventTarget.prototype.removeEventListener=function(type,fn,o){if(track(this))entries.get(key(this,type,o))?.delete(fn);return remove.call(this,type,fn,o)};
 window.xyListenerCount=()=>[...entries.values()].reduce((n,s)=>n+s.size,0);
})()'''

class XY(Cubes):
 def setUp(self):
  super().setUp();self.page.add_init_script(TRACK);self.page.reload();self.page.wait_for_function('window.ready');self.page.evaluate('window.ng=window.jefferiesNavigation');self.baseline=self.page.evaluate('xyListenerCount()')
 def open_xy(self,options=None,animate=False):
  config={'entity':'light.zone_a','anchor_x':self.viewport['width']/2,'anchor_y':self.viewport['height']/2,'animate':animate,'center_button':False,'empty_slots':'hidden','buttons':[{'slot':1,'icon':'mdi:circle','tap_action':{'action':'none'}}],
   'xy_pad':{'x':{'service':'light.turn_on','data':{'brightness_step':'JTSJS: return variables.x;'}},**(options or {})}}
  self.page.evaluate('config=>{window.xyMenu=ng.open(config)}',config);self.page.wait_for_function('xyMenu.shadowRoot.querySelector("jts-n-xy-pad")?.joystick');self.settle();self.page.evaluate("window.pad=xyMenu.shadowRoot.querySelector('jts-n-xy-pad')")
  return self.page.locator('jts-n-xy-pad')
 def start(self):
  box=self.page.locator('jts-n-xy-pad #joystick').bounding_box();self.page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2);self.page.mouse.down();self.page.mouse.move(box['x']+box['width']/2+15,box['y']+box['height']/2,steps=2)
 def assert_stopped(self):
  self.assertTrue(self.page.evaluate('!pad.active && !pad._interval'))
  count=self.page.evaluate('calls.length');self.page.wait_for_timeout(120);self.assertEqual(self.page.evaluate('calls.length'),count)
 def test_repeat_stops_at_close_including_animation_and_direct_dispose(self):
  for mode in ['close','animated','dispose','remove']:
   self.open_xy({'repeat':30},animate=mode=='animated');self.start();self.page.wait_for_timeout(80);self.assertGreater(self.page.evaluate('calls.length'),0)
   self.page.evaluate({'close':'ng.close()','animated':'ng.close()','dispose':'ng.disposeContext(xyMenu._menuContext)','remove':'xyMenu.remove()'}[mode]);self.assert_stopped();self.page.mouse.up();self.assert_stopped()
   self.settle();self.assertFalse(self.page.evaluate('pad.isConnected'));self.assertEqual(self.page.evaluate('xyListenerCount()'),self.baseline);self.page.evaluate('ng.disposeContext(xyMenu._menuContext);calls.length=0')
 def test_normal_mouse_touch_on_release_and_exact_payload(self):
  self.open_xy();self.start();expected=self.page.evaluate('pad._current.x');self.assertAlmostEqual(expected,15,delta=.5);self.page.mouse.up();self.assertGreater(self.page.evaluate('calls.length'),0)
  self.assertEqual(self.page.evaluate('calls.at(-1).slice(0,2)'),['light','turn_on']);self.assertEqual(self.page.evaluate('calls.at(-1)[2].brightness_step'),expected);self.assert_stopped();self.capture('xy-normal-mouse');self.page.evaluate('ng.close();calls.length=0')
  self.open_xy({'on_release':True});self.start();expected=self.page.evaluate('pad._current.x');self.assertEqual(self.page.evaluate('calls.length'),0);self.page.mouse.up();self.assertEqual(self.page.evaluate('calls.length'),1);self.assertEqual(self.page.evaluate('calls[0][2].brightness_step'),expected)
  self.page.evaluate("document.dispatchEvent(new MouseEvent('mouseup',{bubbles:true}))");self.assertEqual(self.page.evaluate('calls.length'),1);self.page.evaluate('ng.close();calls.length=0')
  self.open_xy({'on_release':True});self.page.evaluate("()=>{pad.dispatchEvent(new TouchEvent('touchstart',{bubbles:true}));const r=pad.getBoundingClientRect();pad.dispatchEvent(new TouchEvent('touchmove',{bubbles:true,targetTouches:[new Touch({identifier:1,target:pad,clientX:r.left+pad.joystick.offsetLeft+pad.size/2+12,clientY:r.top+pad.joystick.offsetTop+pad.size/2,pageX:r.left+pad.joystick.offsetLeft+pad.size/2+12,pageY:r.top+pad.joystick.offsetTop+pad.size/2})]}));document.dispatchEvent(new TouchEvent('touchend',{bubbles:true}))}")
  self.assertEqual(self.page.evaluate('calls.length'),1);self.assertEqual(self.page.evaluate('calls[0][2].brightness_step'),12);self.capture('xy-normal-touch');self.page.evaluate('ng.close()')
 def test_cancel_never_applies_on_release_and_repeat_does_not_resume(self):
  for event in ['touchcancel','pointercancel','blur','hidden','detach','config']:
   self.open_xy({'on_release':True});self.start();self.assertEqual(self.page.evaluate('calls.length'),0)
   self.page.evaluate({'touchcancel':"document.dispatchEvent(new Event('touchcancel'))",'pointercancel':"document.dispatchEvent(new Event('pointercancel'))",'blur':"window.dispatchEvent(new Event('blur'))",'hidden':"Object.defineProperty(document,'hidden',{configurable:true,value:true});document.dispatchEvent(new Event('visibilitychange'))",'detach':'pad.remove()', 'config':'pad.config={...pad.config}'}[event]);self.settle();self.assert_stopped();self.page.mouse.up();self.assertEqual(self.page.evaluate('calls.length'),0)
   self.page.evaluate("Object.defineProperty(document,'hidden',{configurable:true,value:false});ng.disposeContext(xyMenu._menuContext)")
  self.open_xy({'repeat':30});self.start();self.page.wait_for_timeout(50);self.page.evaluate("window.dispatchEvent(new Event('blur'))");self.assert_stopped();self.page.mouse.up();self.assert_stopped();self.page.evaluate('ng.close()')
 def test_preview_Info_and_late_events_cannot_dispatch(self):
  self.open_xy({'repeat':30});self.start();self.page.wait_for_timeout(60)
  self.page.evaluate("ng.openInfoInContext(xyMenu._menuContext,{title:'Suspended XY',text:'Read only'})");self.assert_stopped();count=self.page.evaluate('calls.length')
  self.page.evaluate("xyMenu._handleXYPad({type:'jts-n-drag-interval',detail:{x:15,y:0}})");self.assertEqual(self.page.evaluate('calls.length'),count);self.page.mouse.up();self.page.locator('jts-n-info-cube .surface').press('Escape');self.assert_stopped();self.capture('xy-after-Info-return')
  self.page.evaluate('xyMenu._menuContext.owner={preview:true}');self.start();self.assert_stopped();self.page.mouse.up();self.page.evaluate("xyMenu._handleXYPad({type:'jts-n-drag-interval',detail:{x:15,y:0}})");self.assertEqual(self.page.evaluate('calls.length'),count)
  self.page.evaluate('xyMenu._menuContext.owner=null;ng.close()');self.page.evaluate("xyMenu._handleXYPad({type:'jts-n-drag-interval',detail:{x:15,y:0}})");self.assertEqual(self.page.evaluate('calls.length'),count)
 def test_repeated_teardown_and_reconnect_have_no_listener_growth(self):
  self.page.evaluate("async()=>{const transient=document.createElement('jts-n-xy-pad');transient.config={x:{}};transient.size=20;document.body.append(transient);transient.remove();await transient.updateComplete}");self.assertEqual(self.page.evaluate('xyListenerCount()'),self.baseline)
  for i in range(20):
   self.open_xy({'repeat':30});self.page.evaluate("pad._handleOnDragStart(new MouseEvent('mousedown'));pad._handleOnDragStart(new MouseEvent('mousedown'));pad._setPosition(pad.joystick.offsetLeft+pad.size/2+5,pad.joystick.offsetTop+pad.size/2)");self.page.evaluate('ng.close()');self.assert_stopped();self.assertEqual(self.page.evaluate('xyListenerCount()'),self.baseline)
  self.open_xy({'on_release':True});before=self.page.evaluate('xyListenerCount()');self.page.evaluate('window.parentPad=pad.parentNode;pad.remove()');self.assertEqual(self.page.evaluate('xyListenerCount()'),before-6)
  self.page.evaluate('parentPad.append(pad)');self.settle();self.assertEqual(self.page.evaluate('xyListenerCount()'),before);self.start();self.page.mouse.up();self.assertGreater(self.page.evaluate('calls.length'),0);self.page.evaluate('ng.close()');self.assertEqual(self.page.evaluate('xyListenerCount()'),self.baseline)

def main():
 p=argparse.ArgumentParser();p.add_argument('--bundle',type=Path,required=True);p.add_argument('--button-card',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--test-filter');a=p.parse_args();a.evidence_dir.mkdir(parents=True,exist_ok=True)
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);server.bundle=a.bundle.resolve();server.button=a.button_card.resolve();threading.Thread(target=server.serve_forever,daemon=True).start();ok=True
 try:
  with sync_playwright() as runtime:
   XY.browser=runtime.chromium.launch(executable_path=os.getenv('CHROMIUM_PATH') or shutil.which('chromium'),args=['--no-sandbox']);XY.url=f'http://127.0.0.1:{server.server_port}';XY.evidence=a.evidence_dir
   for width,height in [(390,844),(1440,900)]:
    XY.viewport={'width':width,'height':height};names=[n for n in XY.__dict__ if n.startswith('test_') and (not a.test_filter or a.test_filter in n)];result=unittest.TextTestRunner(verbosity=2,resultclass=CheckResult).run(unittest.TestSuite(XY(n) for n in names));ok=result.wasSuccessful() and ok
   XY.browser.close()
 finally:server.shutdown();server.server_close()
 return 0 if ok else 1
if __name__=='__main__':raise SystemExit(main())
