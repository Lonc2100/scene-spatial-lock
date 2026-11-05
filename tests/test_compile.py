import importlib.util,tempfile,unittest,json
from pathlib import Path
spec=importlib.util.spec_from_file_location('compiler',Path(__file__).resolve().parents[1]/'scripts/compile_lock.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class CompileContract(unittest.TestCase):
 def test_unknown_person_and_review_not_claimed(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);image=p/'reference.bin';image.write_bytes(b'fixture')
   s=dict(reference_image=str(image),time_place='同一日间，同一书房',anchors=[dict(id='desk',name='书桌',relation='窗前',evidence='author')],axis_lock='入口朝窗',unknown_regions=[],shots=[])
   text=m.compile_scene(s,p/'out');self.assertNotIn('本例无人',text);self.assertIn('未提供',text);r=json.loads((p/'out/空间锁编译回执.json').read_text(encoding='utf-8'));self.assertIn('未提供',r['visual_understanding'])
 def test_reverse_requires_basis_and_preserves_character(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);image=p/'reference.bin';image.write_bytes(b'fixture')
   s=dict(reference_image=str(image),time_place='同一书房',anchors=[dict(id='desk',name='书桌',relation='窗前',evidence='author')],axis_lock='镜头一朝窗，镜头二朝入口，人物状态不重置',unknown_regions=[],shots=[],axis_mode='reverse_views',route='李白侧立桌旁。')
   with self.assertRaises(ValueError):m.compile_scene(s,p/'rejected')
   s['back_view_basis']='作者明确背面中央双扇门';text=m.compile_scene(s,p/'out');self.assertIn('李白',text);self.assertNotIn('无人',text);self.assertIn('镜头二朝入口',text)
if __name__=='__main__':unittest.main()
