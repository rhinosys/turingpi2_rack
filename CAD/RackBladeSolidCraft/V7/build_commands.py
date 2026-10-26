"""V7: 60 mm side walls and interleaved fingers replace the V5 screwed splices.
Filament pins retain the interlock; floor overlap and walls carry the joint loads.
Nominal 1.75 mm filament / 2.1 mm bores require an actual PETG tolerance test.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
C=[]
def cmd(c,**p):C.append(dict(command=c,params=p))
def box(n,x,y,z,l,w,h,op='new',t=None):
 p=dict(name=n,body_name=n,corner=[x,y,z],length=l,width=w,height=h,operation=op)
 if t:p['targets']=t
 cmd('solid.box',**p)
def cyl(n,x,y,z,d,h,op,t=None):
 p=dict(name=n,body_name=n,base=[x,y,z],diameter=d,height=h,axis='Z',operation=op)
 if t:p['targets']=t
 cmd('solid.cylinder',**p)
def save(n):
 (P/n).write_text(json.dumps(dict(name='batch',arguments=dict(commands=C,rollback=True,verbose=False)),indent=2));C.clear()
cmd('component.activate',component='root')
cmd('solid.remove',bodies=[f'ECLISSE-{s}-{i}' for s in ['D','G'] for i in [1,2]])
save('00-remove-splices.json')
for side,s in [('D',1),('G',-1)]:
 def X(x,l):return x if s==1 else -x-l
 front='BT-'+side;rear='FOND-AR-'+side
 # Close only old splice fastener holes; equipment/faceplate fasteners remain.
 for x in [15,193]:
  for y in [184,195,251,269]:cyl(f'Fermer-M3-{side}-{x}-{y}',s*x,y,16,3.8,3 if y<201 else 4,'join',[front if y<201 else rear])
 # The new tall side walls replace the underside ribs: keep a flat print base.
 box('Dessous-plan-'+side,-210,-1,13,420,211,3,'cut',[front])
 # Integral overlapping floor tongue; its receiving step leaves 0.2 mm vertical clearance.
 box('Recouvrement-'+side,X(12,184),200.8,16,184,6.4,2,'join',[front])
 box('Logement-recouvrement-'+side,X(11.8,184.4),201.3,15.9,184.4,6.1,2.3,'cut',[rear])
 for i,x in enumerate([5.5,196.5],1):
  box(f'Muret-AV-{side}-{i}',X(x,6),6,18.8,6,191.2,60.2,'join',[front])
  box(f'Muret-AR-{side}-{i}',X(x,6),205.2,19.8,6,214.8,59.2,'join',[rear])
  for k in range(8):
   target=front if k%2==0 else rear
   y=197.0 if k%2==0 else 197.4
   box(f'Doigt-{side}-{i}-{k}',X(x,6),y,20+k*7.4,6,8,7.1,'join',[target])
  cyl(f'Passage-filament-{side}-{i}',s*(x+3),201.2,21.2,2.1,61,'cut',[front,rear])
  pin=f'REF_FILAMENT-{side}-{i}'
  cyl(pin,s*(x+3),201.2,21.3,1.75,61,'new')
  cmd('component.move_bodies',bodies=[pin],component='CASSETTE-'+side)
 save('01-walls-'+side+'.json')
cmd('document.metadata.set',values=dict(revision='V7',description='Cassettes à murets 60 mm, doigts entrelacés et verrouillage filament 1.75 mm; châssis V6 conservé.'))
save('02-metadata.json')
