"""Validate fitted source and the rebuilt SolidCraft timeline before publishing."""
from pathlib import Path
import json,zipfile,math,collections
P=Path(__file__).resolve().parent
def read(stem):return json.loads(json.loads((P/'verification'/f'{stem}.json').read_text())['result']['content'][0]['text'])
a=read('inspect-repaired');m=read('measure-repaired')
errors=[x for x in a['timeline'] if x.get('error')]
assert not errors,errors
assert len(m['bodies'])==46
assert all(b['kernel']['shells']==1 for b in m['bodies'])
expected={'m3_clear':3.2,'m4_clear':4.3,'m3_nut_af':5.7,'m4_nut_af':7.2,'bisc_clear':0.2}
with zipfile.ZipFile(P/'V7_calibre.solidcraft') as z:d=json.loads(z.read('document.json'))
params={p['name']:p['expr'] for p in d['params']}
for k,v in expected.items():assert float(params[k])==v,(k,params[k])
hexes=[]
for f in d['features']:
 if f['type']=='sketch' and 'nut' in f['name'].lower():
  c=next(c for c in f['sketch']['curves'] if c['type']=='circle')
  af=c['r']*math.sqrt(3);assert min(abs(af-5.7),abs(af-7.2))<1e-6
  hexes.append(dict(feature=f['id'],name=f['name'],across_flats_mm=af))
assert len(hexes)==57
result=dict(bodies=46,single_shell_bodies=46,features=len(d['features']),feature_errors=errors,parameters=expected,nut_sketches=hexes,warning_count=sum(bool(t.get('warning')) for t in a['timeline']),scope='Full candidate reopened; legacy entry relief suppressed and recomputed; source and bodies verified. No second full reopen after save.')
(P/'verification/native-validation.json').write_text(json.dumps(result,indent=2))
print('Native valid:',len(hexes),'nut sketches, 46 bodies, no feature errors')
