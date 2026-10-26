"""Package only validated delivery files, excluding working/slicing duplicates."""
from pathlib import Path
import json,zipfile,hashlib
P=Path(__file__).resolve().parent;V=P.parent;R=V.parent
reports=json.loads((P/'verification/audit-plateaux.json').read_text());assert len(reports)==11
manifest={}
for f in sorted(P.glob('[0-9][0-9]_*.3mf')):manifest[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
(P/'SHA256.json').write_text(json.dumps(manifest,indent=2))
seconds=sum(int(r['slice']['prediction']) for r in reports[:10]);grams=sum(float(r['slice']['weight']) for r in reports[:10])
p=P/'README.md';s=p.read_text();s=s.split('\n## Estimations de tranchage')[0]
s+='\n## Estimations de tranchage\n\n'
s+=f'Production complète : environ **{seconds//3600} h {(seconds%3600)//60:02d} et {grams/1000:.2f} kg** de PETG, supports et bordures compris selon Bambu Studio. Le plateau optionnel ajoute environ 2 h 07 et 31 g. Les temps réels peuvent varier.\n\n'
s+='| Plateau | Temps estimé | PETG |\n|---|---:|---:|\n'
for r in reports:
 t=int(r['slice']['prediction']);g=float(r['slice']['weight'])
 s+=f"| {r['file']} | {t//3600} h {(t%3600)//60:02d} | {g:.0f} g |\n"
s+='\nLes 11 projets ont été tranchés localement avec Bambu Studio 02.08.02.60. Aucun objet n’est ignoré ou hors plateau ; les empreintes de première couche incluent supports et bordures et laissent libre la zone de calibration avant. Le CLI émet un message de recherche de variante d’extrudeur ; il termine avec succès et les sorties contrôlées utilisent un seul PETG noir, avec la buse standard 0,4 mm. Les journaux sont conservés.\n'
p.write_text(s)
files=list(P.glob('[0-9][0-9]_*.3mf'))+list(P.glob('*.png'))+[P/'README.md',P/'inventaire.json',P/'SHA256.json',P/'verification/audit-plateaux.json']
with zipfile.ZipFile(V/'Plateaux_V7_PETG_noir.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in files:z.write(f,f.relative_to(P))
with zipfile.ZipFile(V/'V7_Complet_PETG_noir.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in [R/'RackTuringPi2_Complet_V7.solidcraft',V/'README.md',V/'calibration/README.md',V/'Test_filament_V7.solidcraft',V/'Test_jonction_V7.solidcraft']+list((V/'exports').glob('*.3mf'))+list((V/'exports').glob('*.step'))+files:
  z.write(f,f.relative_to(R))
for f in [V/'Plateaux_V7_PETG_noir.zip',V/'V7_Complet_PETG_noir.zip']:
 with zipfile.ZipFile(f) as z:assert z.testzip() is None
 print(f.name,round(f.stat().st_size/1024/1024,1),'MiB')
