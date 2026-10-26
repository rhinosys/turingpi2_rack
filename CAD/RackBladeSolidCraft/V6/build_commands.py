"""V6 integrated tunnels, built on the preserved V5. Millimetres; Y is depth."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=[]
def cmd(command,**params):C.append(dict(command=command,params=params))
def box(n,x,y,z,l,w,h,op,t):cmd('solid.box',name=n,body_name=n,corner=[x,y,z],length=l,width=w,height=h,operation=op,targets=t)
def cyl(n,x,y,z,d,h,axis,t,op='cut'):cmd('solid.cylinder',name=n,body_name=n,base=[x,y,z],diameter=d,height=h,axis=axis,operation=op,targets=t)
def save(n):
 (ROOT/n).write_text(json.dumps(dict(name='batch',arguments=dict(commands=C,rollback=True,verbose=False)),indent=2));C.clear()
cmd('component.activate',component='root')
cmd('solid.remove',bodies=['CL-AV','CL-AR','EAR-D'])
save('00-remove.json')
for side,s in [('D',1),('G',-1)]:
 def X(x,l):return x if s==1 else -x-l
 for pos,y,end in [('AV',0,210),('AR',210.2,424)]:
  q='Q-'+pos+'-'+side+('-EAR' if side=='G' and pos=='AV' else '')
  top='TOP-'+pos+'-'+side
  box('Rive-plane-'+q,-250,y-6,-.1,500,6,177,'cut',[q,top])
  box('Pont-toit-'+q,X(219,4),y,173.3,4,end-y,.4,'join',[q])
  cmd('solid.combine',target=q,tools=[top],operation='join')
  wall='Demi-cloison-'+q
  box(wall,X(.15,4.85),y,3.8,4.85,end-y,169.9,'new',[])
  box('Guide-central-'+q,X(2,3.02),y-.01,16,3.02,end-y+.02,3.4,'cut',[wall])
  for yy in ([50,130] if pos=='AV' else [290,370]):
   box('Biscuit-central-'+q+str(yy),-11.05,yy-10.05,173.25,22.1,20.1,3.4,'cut',[wall])
  box('Biscuit-croix-'+q,-11.05,198.95,173.25,22.1,22.1,3.4,'cut',[wall])
  cmd('solid.combine',target=q,tools=[wall],operation='join')
  for yy in ([30,105,180] if pos=='AV' else [240,315,390]):
   cyl('Obturation-toit-'+q+str(yy),X(214.8,8.3),yy,166,8.6,8.3,'X',[q],'join')
  for yy in ([25,90,170,195] if pos=='AV' else [240,310,390,410]):
   cyl('Obturation-cloison-'+q+str(yy),s*12.5,yy,0,5,4,'Z',[q],'join')
  if pos=='AV':
   box('Oreille-integree-'+side,X(211.3,30),0,0,30,5,176.5,'join',[q])
   for zz in [6.35,38.10,66.675,111.125,139.70,171.45]:
    box('Slot-'+side+str(zz),X(230.05,5),-.1,zz-3.5,5,5.2,7,'cut',[q])
    for xx in [230.05,235.05]:cyl('Slot-bout-'+side+str(zz)+str(xx),s*xx,-.1,zz,7,5.2,'Y',[q])
  if pos=='AV' and side=='D':
   # The simpler original quarter accepts the ear before the roof/partition union.
   C[:]=C[:1]+C[16:]+C[1:16]
  save('01-'+pos+'-'+side+'.json')
cmd('document.metadata.set',values={'revision':'V6','description':'Quatre tunnels verticaux intégrés; cassettes V5 complètes; oreilles sur plan Y0.'})
save('02-metadata.json')
