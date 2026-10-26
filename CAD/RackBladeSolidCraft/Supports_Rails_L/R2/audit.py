from pathlib import Path
import json,zipfile,xml.etree.ElementTree as E,numpy as np,trimesh
p=Path(__file__).resolve().parent;N='{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}';reports=[]
for name in ['AV-A','AV-B','AR-A','AR-B']:
 with zipfile.ZipFile(p/'exports'/f'{name}.3mf') as z:t=E.fromstring(z.read('3D/3dmodel.model'))
 m=t.find('.//'+N+'mesh');v=np.array([[float(a.get(k)) for k in ['x','y','z']] for a in m.find(N+'vertices')]);f=np.array([[int(a.get(k)) for k in ['v1','v2','v3']] for a in m.find(N+'triangles')]);mesh=trimesh.Trimesh(v,f,process=False)
 assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0 and abs(v[:,2].min())<.01
 reports.append(dict(part=name,watertight=True,winding_consistent=True,volume_mm3=float(mesh.volume),bounds=mesh.bounds.tolist()))
d=json.loads(json.loads((p/'verification/inspect.json').read_text())['result']['content'][0]['text']);assert not [f for f in d['timeline'] if f.get('error')]
(p/'verification/mesh-audit.json').write_text(json.dumps(reports,indent=2));print(reports)
# Only nominal contact at the two screw heads is accepted from Boolean roundoff.
x=json.loads(json.loads((p/'verification/interference.json').read_text())['result']['content'][0]['text'])
assert not x['budget_exceeded'] and x['pairs_not_checked']==0
for pair in x['interferences']:
 assert pair['a'] in ['AR-A','AR-B'] and pair['b']=='REF-VIS-M4-'+pair['a'][-1]
 assert pair['volume_mm3']<0.01 and pair['bbox']['max'][2]-pair['bbox']['min'][2]<0.001
for stem,expected in [('Plateau_2_arriere_M4_R2',2),('Plateau_4_supports_R2',4)]:
 with zipfile.ZipFile(p/(stem+'_PETG_noir.3mf')) as z:
  d=json.loads(z.read('Metadata/project_settings.config'));assert d['filament_type']==['PETG'] and d['filament_colour']==['#000000'] and d['wall_loops']=='6'
  info=E.fromstring(z.read('Metadata/slice_info.config'));obs=info.findall('./plate/object');assert len(obs)==expected
  assert all(o.get('skipped')=='false' for o in obs)
  assert sum('AR-A' in o.get('name','') for o in obs)==1 and sum('AR-B' in o.get('name','') for o in obs)==1
print('Both plates validated; only nominal screw-head seating contacts in assembly')
