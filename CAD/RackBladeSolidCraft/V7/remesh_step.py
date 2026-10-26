"""Retriangulate selected SolidCraft STEP exports with Gmsh/OCC; leave native CAD unchanged.
Dependencies: gmsh 4.15.2, trimesh 4.12.2, numpy. Raw 3MF exports are preserved.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as E,json,shutil,tempfile
import sys
import numpy as np
import trimesh,gmsh
root=Path(__file__).resolve().parent
ns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
tag=lambda s:"{"+ns+"}"+s
E.register_namespace("",ns)
measure={b["name"]:b for b in json.loads(json.loads((root/"verification/measure-final-v7.json").read_text())["result"]["content"][0]["text"])["bodies"]}
audit={x["file"]:x for x in json.loads((root/"verification/3mf-audit.json").read_text())}
raw=root/"verification/original-3mf";raw.mkdir(exist_ok=True)
reports=[]
for name in (sys.argv[1:] or ["BT-D","BT-G","FOND-AR-D","FOND-AR-G"]):
    dest=root/"exports"/(name+".3mf");backup=raw/dest.name
    if not backup.exists():shutil.copy2(dest,backup)
    gmsh.initialize();gmsh.option.setNumber("General.Terminal",0)
    gmsh.model.occ.importShapes(str(root/"exports"/(name+"_print.step")))
    gmsh.model.occ.removeAllDuplicates()
    gmsh.model.occ.healShapes(tolerance=0.001, fixDegenerated=True, fixSmallEdges=True, fixSmallFaces=True, sewFaces=True, makeSolids=True)
    gmsh.model.occ.synchronize()
    occ_vol=sum(gmsh.model.occ.getMass(3,t) for d,t in gmsh.model.getEntities(3))
    gmsh.option.setNumber("Mesh.MeshSizeMax",5)
    gmsh.option.setNumber("Mesh.MeshSizeMin",0.1)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature",64)
    gmsh.model.mesh.generate(2)
    with tempfile.TemporaryDirectory() as td:
        stl=Path(td)/"part.stl";gmsh.write(str(stl));gmsh.finalize()
        mesh=trimesh.load(stl,force="mesh",process=True)
    # These three quadrants retain XYZ print orientation; translate only.
    mesh.merge_vertices(digits_vertex=4)
    trimesh.repair.fill_holes(mesh)
    mesh.fix_normals(multibody=True) # Consistent triangle orientation after OCC healing
    expected=measure[name]["volume_mm3"]
    delta=abs(mesh.volume-expected)/expected
    lo=np.array(audit[name+".3mf"]["bbox_min"]); expected_bounds=np.array([lo,lo+np.array(audit[name+".3mf"]["dimensions"])])
    bd=float(np.max(np.abs(mesh.bounds-expected_bounds)))
    report={"name":name,"method":"Gmsh/OCC triangulation of SolidCraft STEP","watertight":bool(mesh.is_watertight),"winding_consistent":bool(mesh.is_winding_consistent),"solidcraft_volume_mm3":expected,"occ_import_volume_mm3":occ_vol,"mesh_volume_mm3":float(mesh.volume),"relative_volume_delta":float(delta),"bbox_max_delta_mm":bd,"vertices":len(mesh.vertices),"triangles":len(mesh.faces)}
    
    if not mesh.is_watertight:
        counts=np.bincount(mesh.edges_unique_inverse);bad=mesh.edges_unique[counts!=2]; print("BAD",len(bad),mesh.vertices[bad[:12]].tolist(),flush=True)
        mesh.export(str(root/"verification"/(name+"-debug.ply")))
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume>0,report
    assert delta<0.0002 and bd<0.01,report
    with zipfile.ZipFile(backup) as z:contents={n:z.read(n) for n in z.namelist()}
    modelname=next(n for n in contents if n.endswith(".model"))
    tree=E.fromstring(contents[modelname]);m=tree.find(".//"+tag("mesh"))
    vv=m.find(tag("vertices"));ff=m.find(tag("triangles"));vv.clear();ff.clear()
    for p in mesh.vertices:E.SubElement(vv,tag("vertex"),{k:format(float(n),".12g") for k,n in zip(("x","y","z"),p)})
    for p in mesh.faces:E.SubElement(ff,tag("triangle"),{k:str(int(n)) for k,n in zip(("v1","v2","v3"),p)})
    contents[modelname]=E.tostring(tree,encoding="utf-8",xml_declaration=True)
    with zipfile.ZipFile(dest,"w",zipfile.ZIP_DEFLATED) as z:
        for n,data in contents.items():z.writestr(n,data)
    (root/"verification"/("mesh-"+name+".json")).write_text(json.dumps(report,indent=2))
    reports.append(report)
    print(json.dumps(report),flush=True)
(root/"verification/mesh-repair.json").write_text(json.dumps(reports,indent=2))
