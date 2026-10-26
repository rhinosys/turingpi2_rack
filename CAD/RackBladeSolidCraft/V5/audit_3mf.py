"""Audit exported 3MF bounding boxes and edge incidence using only Python's standard library."""
from pathlib import Path
import zipfile, xml.etree.ElementTree as E, json, collections
import numpy as np
root=Path(__file__).resolve().parent
ns={"m":"http://schemas.microsoft.com/3dmanufacturing/core/2015/02"}
results=[]
for p in sorted((root/"exports").glob("*.3mf")):
    with zipfile.ZipFile(p) as z:
        tree=E.fromstring(z.read(next(n for n in z.namelist() if n.endswith(".model"))))
    objects=[];allverts=[]
    for o in tree.findall(".//m:object",ns):
        verts=[tuple(float(v.get(c)) for c in ("x","y","z")) for v in o.findall(".//m:vertex",ns)]
        tris=[tuple(int(t.get(c)) for c in ("v1","v2","v3")) for t in o.findall(".//m:triangle",ns)]
        if not verts: continue
        edges=collections.Counter(tuple(sorted((t[i],t[(i+1)%3]))) for t in tris for i in range(3))
        directed=collections.Counter((t[i],t[(i+1)%3]) for t in tris for i in range(3))
        v=np.array(verts);f=np.array(tris);volume=float(np.einsum("ij,ij->i",v[f[:,0]],np.cross(v[f[:,1]],v[f[:,2]])).sum()/6)
        allverts.extend(verts)
        objects.append({"id":o.get("id"),"vertices":len(verts),"triangles":len(tris),"nonmanifold_edges":sum(n!=2 for n in edges.values()),"inconsistent_winding_edges":sum(n!=1 for n in directed.values()),"signed_volume_mm3":volume})
    assert allverts,p
    items=tree.findall("m:build/m:item",ns)
    assert all(i.get("transform") in (None,"1 0 0 0 1 0 0 0 1 0 0 0") for i in items),"Audit expects baked coordinates"
    lo=[min(v[i] for v in allverts) for i in range(3)]
    hi=[max(v[i] for v in allverts) for i in range(3)]
    dim=[hi[i]-lo[i] for i in range(3)]
    results.append({"file":p.name,"unit":tree.get("unit"),"objects":objects,"build_items":len(items),"bbox_min":lo,"dimensions":dim,"fits":all(d<=lim+.01 for d,lim in zip(dim,[240,240,210])),"on_bed":abs(lo[2])<.01})
(root/"verification/3mf-audit.json").write_text(json.dumps(results,indent=2))
bad=[r["file"] for r in results if not r["on_bed"] or any(o["nonmanifold_edges"] or o["inconsistent_winding_edges"] or o["signed_volume_mm3"]<=0 for o in r["objects"])]
print(json.dumps({"files":len(results),"mesh_failures":bad,"exceeds_conservative_envelope":[r["file"] for r in results if not r["fits"]]},indent=2))
