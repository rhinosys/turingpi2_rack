from pathlib import Path
import zipfile,json,xml.etree.ElementTree as E,tempfile,shutil
import gmsh,trimesh,numpy as np
P=Path(__file__).resolve().parent;N='http://schemas.microsoft.com/3dmanufacturing/core/2015/02';T=lambda x:'{'+N+'}'+x
E.register_namespace('',N)
name='AR-B';dest=P/'exports'/f'{name}.3mf';backup=P/'verification/AR-B_original.3mf'
if not backup.exists():shutil.copy2(dest,backup)
with zipfile.ZipFile(backup) as z:entries={n:z.read(n) for n in z.namelist()}
tree=E.fromstring(entries['3D/3dmodel.model']);meshxml=tree.find('.//'+T('mesh'));v0=np.array([[float(v.get(k)) for k in ['x','y','z']] for v in meshxml.find(T('vertices'))]);bounds=np.array([v0.min(0),v0.max(0)])
d=json.loads(json.loads((P/'verification/measure.json').read_text())['result']['content'][0]['text']);vol=next(b['volume_mm3'] for b in d['bodies'] if b['name']==name)
gmsh.initialize();gmsh.option.setNumber('General.Terminal',0);gmsh.model.occ.importShapes(str(P/'exports'/f'{name}.step'));gmsh.model.occ.healShapes(tolerance=.001);gmsh.model.occ.synchronize();gmsh.option.setNumber('Mesh.MeshSizeMax',2);gmsh.option.setNumber('Mesh.MeshSizeMin',.1);gmsh.option.setNumber('Mesh.MeshSizeFromCurvature',64);gmsh.model.mesh.generate(2)
with tempfile.TemporaryDirectory() as td:
 f=Path(td)/'m.stl';gmsh.write(str(f));gmsh.finalize();mesh=trimesh.load(f,force='mesh',process=True)
mesh.merge_vertices(digits_vertex=5);trimesh.repair.fill_holes(mesh);mesh.fix_normals(multibody=True)
report=dict(watertight=bool(mesh.is_watertight),consistent=bool(mesh.is_winding_consistent),relative_volume_error=abs(mesh.volume-vol)/vol,bounds_error_mm=float(np.max(np.abs(mesh.bounds-bounds))))
assert report['watertight'] and report['consistent'] and report['relative_volume_error']<.0002 and report['bounds_error_mm']<.01,report
vv=meshxml.find(T('vertices'));ff=meshxml.find(T('triangles'));vv.clear();ff.clear()
for v in mesh.vertices:E.SubElement(vv,T('vertex'),dict(zip(['x','y','z'],[format(x,'.12g') for x in v])))
for f in mesh.faces:E.SubElement(ff,T('triangle'),dict(zip(['v1','v2','v3'],map(str,f))))
entries['3D/3dmodel.model']=E.tostring(tree,encoding='utf-8',xml_declaration=True)
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
 for n,data in entries.items():z.writestr(n,data)
(P/'verification/remesh-AR-B.json').write_text(json.dumps(report,indent=2));print(report)
