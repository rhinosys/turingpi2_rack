"""Check final 3MF shells, winding, volume agreement and print envelope.
Run with Python plus trimesh and numpy; does not modify the exported geometry.
"""
from pathlib import Path
import json
import zipfile
import xml.etree.ElementTree as E
import trimesh

root = Path(__file__).resolve().parents[1]
ns = {'m': 'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
with zipfile.ZipFile(root / 'Rack_Tolerance_PETG_R1.3mf') as z:
    tree = E.fromstring(z.read(next(n for n in z.namelist() if n.endswith('.model'))))
assert tree.get('unit') == 'millimeter'
assert all(i.get('transform') in (None, '1 0 0 0 1 0 0 0 1 0 0 0')
           for i in tree.findall('m:build/m:item', ns))
reports = []
for obj in tree.findall('.//m:object', ns):
    vertices = [[float(v.get(k)) for k in ('x', 'y', 'z')]
                for v in obj.findall('.//m:vertex', ns)]
    faces = [[int(t.get(k)) for k in ('v1', 'v2', 'v3')]
             for t in obj.findall('.//m:triangle', ns)]
    if not vertices:
        continue
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=True)
    report = dict(id=obj.get('id'), name=obj.get('name'),
                  watertight=bool(mesh.is_watertight),
                  winding_consistent=bool(mesh.is_winding_consistent),
                  volume_mm3=float(mesh.volume), bounds=mesh.bounds.tolist())
    reports.append(report)
    assert mesh.is_watertight and mesh.is_winding_consistent and mesh.volume > 0, report
    assert abs(mesh.bounds[0][2]) < 0.001, report
    assert all(a >= -0.001 for a in mesh.bounds[0]), report
    assert all(a <= b + 0.001 for a, b in zip(mesh.bounds[1], [240, 240, 210])), report
assert len(reports) == 11
cad = json.loads((root / 'verification/measure.json').read_text())
relative_delta = abs(sum(r['volume_mm3'] for r in reports) - cad['total']['volume_mm3']) / cad['total']['volume_mm3']
# Native triangulation approximates circular holes and curved glyphs.
# Allow 0.02 percent total volume difference; exact geometry is in the STEP.
assert relative_delta < 0.0002, relative_delta
out = {'objects': reports, 'relative_volume_delta': relative_delta, 'passed': True}
(root / 'verification/mesh-audit.json').write_text(json.dumps(out, indent=2))
print(json.dumps({'objects': len(reports), 'relative_volume_delta': relative_delta, 'passed': True}))
