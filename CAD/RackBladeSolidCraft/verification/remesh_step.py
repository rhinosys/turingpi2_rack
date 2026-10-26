"""Retriangulate selected SolidCraft STEP exports with Gmsh/OCC; leave native CAD unchanged.
Dependencies: gmsh 4.15.2, trimesh 4.12.2, numpy. Raw 3MF exports are preserved.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as E,json,shutil,tempfile
import numpy as np
import trimesh,gmsh
root=Path(__file__).resolve().parents[1]
ns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
tag=lambda s:"{"+ns+"}"+s
E.register_namespace("",ns)
measure={b["name"]:b for b in json.loads((root/"verification/measure-print.json").read_text())}
raw=root/"verification/original-3mf";raw.mkdir(exist_ok=True)
reports=[]
for name in ["Q-AV-D","Q-AV-G","Q-AR-D"]:
    dest=root/"exports/3mf"/(name+".3mf");backup=raw/dest.name
    if not backup.exists():shutil.copy2(dest,backup)
    gmsh.initialize();gmsh.option.setNumber("General.Terminal",0)
    gmsh.model.occ.importShapes(str(root/"exports/step"/(name+".step")))
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
    assert measure[name]["angle"]==0
    mesh.apply_translation(measure[name]["translate"])
    expected=measure[name]["volume_mm3"]
    delta=abs(mesh.volume-expected)/expected
    expected_bounds=np.array([measure[name]["bbox"]["min"],measure[name]["bbox"]["max"]])
    bd=float(np.max(np.abs(mesh.bounds-expected_bounds)))
    report={"name":name,"method":"Gmsh/OCC triangulation of SolidCraft STEP","watertight":bool(mesh.is_watertight),"winding_consistent":bool(mesh.is_winding_consistent),"solidcraft_volume_mm3":expected,"occ_import_volume_mm3":occ_vol,"mesh_volume_mm3":float(mesh.volume),"relative_volume_delta":float(delta),"bbox_max_delta_mm":bd,"vertices":len(mesh.vertices),"triangles":len(mesh.faces)}
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
    reports.append(report)
    print(json.dumps(report),flush=True)
(root/"verification/mesh-repair.json").write_text(json.dumps(reports,indent=2))
