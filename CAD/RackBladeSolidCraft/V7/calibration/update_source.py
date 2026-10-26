"""Apply the user's measured fits once, then rebuild the candidate through SolidCraft.
J and X are TOTAL biscuit XY clearances. No inferred guide or filament change.
Hex nut sketches in the inherited model store numeric construction geometry;
update their actual vertices as well as the human-readable nut parameters.
"""
from pathlib import Path
import json,zipfile,math,shutil
P=Path(__file__).resolve().parent
source=P.parents[1]/'RackTuringPi2_Complet_V7.solidcraft'
backup=P/'V7_avant_calibration.solidcraft'
if not backup.exists():shutil.copy2(source,backup)
with zipfile.ZipFile(backup) as z:contents={n:z.read(n) for n in z.namelist()}
d=json.loads(contents['document.json']);changes=[]
values={'m3_clear':'3.2','m4_clear':'4.3','m3_nut_af':'5.7','m4_nut_af':'7.2','bisc_clear':'0.2'}
for p in d['params']:
 if p['name'] in values:
  changes.append(dict(kind='parameter',name=p['name'],before=p['expr'],after=values[p['name']]))
  p['expr']=values[p['name']]
for f in d['features']:
 if f['type']=='cylinder' and f.get('operation')=='cut':
  r=f.get('radius','')
  if r in ['(3.4 mm) / 2','(4.5 mm) / 2']:
   new='(m3_clear) / 2' if '3.4' in r else '(m4_clear) / 2'
   changes.append(dict(kind='literal_hole',id=f['id'],name=f['name'],before=r,after=new));f['radius']=new
 if f['type']=='sketch' and 'nut' in f.get('name','').lower():
  sk=f['sketch'];circles=[c for c in sk['curves'] if c['type']=='circle']
  assert len(circles)==1,f['name']
  c=circles[0];old=c['r']*math.sqrt(3)
  assert min(abs(old-5.8),abs(old-7.3))<1e-7,(f['name'],old)
  new=5.7 if old<6 else 7.2;factor=new/old;center=sk['points'][c['c']]['pos'][:]
  for p in sk['points']:
   if p['id']!='origin':p['pos']=[center[i]+factor*(p['pos'][i]-center[i]) for i in range(2)]
  c['r']*=factor
  changes.append(dict(kind='nut_sketch',id=f['id'],name=f['name'],before_af=old,after_af=new))
# The calibrated Boolean result is collision-free without the old numerical
# entry relief. Suppress this failing legacy operation; retain it for audit.
for f in d['features']:
 if f['id']==909:
  f['suppressed']=True
  changes.append(dict(kind='suppressed_legacy_relief',id=909,reason='calibrated body collision-free without legacy numerical cut'))
d['name']='RackTuringPi2_Complet_V7_calibre'
d['metadata'].update(revision='V7-calibre',calibration='2026-10-25: PETG HF noir, X1C 0.4, PEI lisse; ajustements sans retouche; J/X total 0.2, D3 3.2, D4 4.3, M3 AF5.7, M4 AF7.2')
contents['document.json']=json.dumps(d,ensure_ascii=False).encode()
with zipfile.ZipFile(P/'V7_candidat.solidcraft','w',zipfile.ZIP_DEFLATED) as z:
 for n,b in contents.items():z.writestr(n,b)
(P/'verification/source-changes.json').write_text(json.dumps(changes,indent=2))
print({k:sum(c['kind']==k for c in changes) for k in ['parameter','literal_hole','nut_sketch']})
