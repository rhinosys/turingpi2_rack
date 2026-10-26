"""Audit final Bambu project geometry, settings, plate assignment and slice output."""
from pathlib import Path
import zipfile,json,xml.etree.ElementTree as E,collections
import numpy as np
P=Path(__file__).resolve().parent
N='{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}'
PN='{http://schemas.microsoft.com/3dmanufacturing/production/2015/06}'
def transform(v,s):
 if not s:return v
 a=np.array(list(map(float,s.split()))).reshape(4,3)
 return v@a[:3]+a[3]
reports=[]
for file in sorted(P.glob('[0-9][0-9]_*.3mf')):
 with zipfile.ZipFile(file) as z:
  d=json.loads(z.read('Metadata/project_settings.config'))
  assert d['filament_type']==['PETG'] and d['filament_colour']==['#000000']
  assert d['curr_bed_type']=='High Temp Plate' and d['layer_height']=='0.16'
  assert d['xy_hole_compensation']=='0' and d['xy_contour_compensation']=='0'
  tree=E.fromstring(z.read('3D/3dmodel.model'))
  def vertices(path,oid):
   t=E.fromstring(z.read(path));o=next(x for x in t.find(N+'resources').findall(N+'object') if x.get('id')==oid)
   mesh=o.find(N+'mesh')
   if mesh is not None:return np.array([[float(v.get(k)) for k in ['x','y','z']] for v in mesh.find(N+'vertices')])
   return np.concatenate([transform(vertices(c.get(PN+'path',path).lstrip('/'),c.get('objectid')),c.get('transform')) for c in o.find(N+'components')])
  ms=E.fromstring(z.read('Metadata/model_settings.config'))
  names={o.get('id'):next(m.get('value') for m in o.findall('metadata') if m.get('key')=='name') for o in ms.findall('object')}
  bodies=[]
  for item in tree.find(N+'build'):
   v=transform(vertices('3D/3dmodel.model',item.get('objectid')),item.get('transform'));lo=v.min(0);hi=v.max(0)
   assert min(lo)>-0.01 and hi[0]<256.01 and hi[1]<256.01 and hi[2]<250.01
   assert abs(lo[2])<0.01 and (lo[0]>=18 or lo[1]>=28)
   bodies.append(dict(name=names[item.get('objectid')],min=lo.tolist(),max=hi.tolist()))
  assert len(ms.findall('./plate/model_instance'))==len(bodies)
  for i,A in enumerate(bodies):
   for B in bodies[:i]:
    assert any(A['min'][k]>=B['max'][k]-.001 or B['min'][k]>=A['max'][k]-.001 for k in [0,1]),(A,B)
  info=E.fromstring(z.read('Metadata/slice_info.config'))
  meta={m.get('key'):m.get('value') for m in info.findall('./plate/metadata')}
  assert 'Metadata/plate_1.gcode' in z.namelist(),'not sliced'
  assert meta.get('outside')=='false' and all(o.get('skipped')=='false' for o in info.findall('./plate/object'))
  assert len(info.findall('./plate/filament'))==1
  footprint=json.loads(z.read('Metadata/plate_1.json'))['bbox_all']
  assert min(footprint)>=0 and max(footprint)<=256.01 and footprint[1]>14,footprint
  reports.append(dict(first_layer_with_supports_and_brim=footprint,file=file.name,objects=bodies,settings='PETG HF noir, X1C 0.4, PEI lisse, couche 0.16',slice=meta))
assert len(reports)==11
counts=collections.Counter(b['name'] for r in reports[:10] for b in r['objects'])
assert counts['BIS']==16 and counts['BIS-X']==2
assert sum(counts.values())==30
(P/'verification/audit-plateaux.json').write_text(json.dumps(reports,indent=2))
print('Validated plates:',len(reports))
