"""Additive V5 history on R4. Coordinates in mm, X width, Y rear, Z up.
The 8 mm lift clears fixed partition feet; hardware envelopes remain provisional.
"""
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
C=[]
def cmd(command,**params):C.append({'command':command,'params':params})
def box(name,x,y,z,l,w,h,op='new',targets=None):
 p=dict(name=name,body_name=name,corner=[x,y,z],length=l,width=w,height=h,operation=op)
 if targets:p['targets']=targets
 cmd('solid.box',**p)
def cyl(name,x,y,z,d,h,axis='Z',targets=None,op='cut'):
 p=dict(name=name,body_name=name,base=[x,y,z],diameter=d,height=h,axis=axis,operation=op)
 if targets:p['targets']=targets
 cmd('solid.cylinder',**p)
def save(name):
 (OUT/name).write_text(json.dumps({'name':'batch','arguments':{'commands':C,'rollback':True,'verbose':False,'timings':True}},indent=2));C.clear()

cmd('component.activate',component='root')
cmd('solid.remove',bodies=['FW-D','FW-G'])
# Existing board platforms and their REF envelopes move together. The facade stays put.
cmd('solid.move',bodies=['BT-D','BT-G','REF_TP2_R','REF_MODULES_R','REF_NVME_R','REF_TP2_L','REF_MODULES_L','REF_NVME_L','REF_FAN_R','REF_FAN_L'],translate=[0,0,8])
cmd('solid.move',bodies=['REF_PSU_R','REF_PSU_L'],translate=[0,0,16])
for side in ['D','G']:
 s=1 if side=='D' else -1
 def X(x,l):return x if s==1 else -x-l
 av='Q-AV-D' if side=='D' else 'Q-AV-G-EAR';ar='Q-AR-'+side
 # Remove obsolete stationary PSU cradles and rear apertures, keeping the 4 mm floor.
 box('Degagement-cassette-'+side,X(5.25,197.5),6,4.01,197.5,414,151.5,'cut',[av,ar])
 box('Cadre-arriere-'+side,X(0,223),420,4,223,4,169.5,'join',[ar])
 box('Passage-arriere-'+side,X(5.2,197.6),419.9,12,197.6,4.2,143.5,'cut',[ar])
 for q,y,depth in [(av,0,210),(ar,210.2,209.8)]:
  rail='RAIL-'+q
  box(rail,X(203,16),y,4,16,depth,18)
  box('Gorge-long-'+q,X(202.8,3.2),y-.1,15.99,3.2,depth+.2,3.42,'cut',[rail,q])
  cmd('solid.combine',target=q,tools=[rail],operation='join')
 # Keep existing facade attachment pattern but move its fastening height to match raised platform.
 box('Bande-IO-rehaussee-'+side,X(21,166),-4,24,166,4,10,'join',['BF-'+side])
 box('Fenetre-IO-V5-'+side,X(24.625,158.75),-4.2,33.6,158.75,4.4,44.45,'cut',['BF-'+side])
 holes=[30,75,135,180] if side=='D' else [-178,-133,-73,-28]
 for x in holes:cyl(f'Vis-facade-V5-{side}-{x}',x,-4.2,25,3.4,10.4,'Y',['BF-'+side])
for cl,y,w in [('CL-AV',0,210),('CL-AR',210,210)]:
 for x in [-5.01,2]:box('Gorge-V5-'+cl+str(x),x,y-.01,16,3.01,w+.02,3.4,'cut',[cl])
save('01-chassis.json')

for side in ['D','G']:
 s=1 if side=='D' else -1
 def X(x,l):return x if s==1 else -x-l
 cmd('component.create',name='CASSETTE-'+side,parent='root')
 rear='FOND-AR-'+side;front='BT-'+side
 box(rear,X(5.5,197),201.4,16,197,218.6,4)
 for x in [2.6,202.5]:box('Langue-'+side+str(x),X(x,2.9),201.4,16.2,2.9,218.6,3,'join',[rear])
 # Fan bulkhead is integral with the removable rear floor, never with the chassis.
 box('Support-ventilateur-'+side,X(5.5,197),212,19.8,197,6,135.2,'join',[rear])
 cyl('Passage-air-'+side,s*104,211.9,82,116,6.2,'Y',[rear])
 for x in [51.5,156.5]:
  for z in [29.5,134.5]:cyl(f'Vis-ventilo-{side}-{x}-{z}',s*x,211.9,z,4.5,6.2,'Y',[rear])
 box('Passage-cables-'+side,X(181,15),211.9,29,15,6.2,27,'cut',[rear])
 # Removable rear panel, surrounding the PSU face and upper exhaust slots.
 box('Paroi-arriere-'+side,X(5.5,197),419.8,16,197,4.2,139,'join',[rear])
 box('Ouverture-PSU-'+side,X(28.5,151),419.9,25.5,151,4.2,87,'cut',[rear])
 for z in [121,132,143]:box('Extraction-air-'+side+str(z),X(15,178),419.9,z,178,4.2,6,'cut',[rear])
 for x in [29,169]:box('Appui-PSU-'+side+str(x),X(x,10),280,19.8,10,140,6.2,'join',[rear])
 for x in [25,179.5]:box('Bord-PSU-'+side+str(x),X(x,3.5),280,19.8,3.5,140,16.2,'join',[rear])
 box('Butee-PSU-'+side,X(29,150),276,19.8,150,3.5,16.2,'join',[rear])
 for x in [20.5,182.5]:
  for y in [300,390]:box(f'Sangle-{side}-{x}-{y}',X(x,5),y,15.9,5,12,4.2,'cut',[rear])
 # Two removable screwed splice bars bridge the printing split under the floor.
 for i,x in enumerate([8,186],1):
  bar=f'ECLISSE-{side}-{i}'
  box(bar,X(x,14),180,12,14,100,4)
  # Clear only underside ribs in this footprint: front floor begins at Z 16.
  box('Logement-'+bar,X(x-.2,14.4),179.8,12,14.4,21.3,4,'cut',[front])
  for y in [184,195,251,269]:
   cyl(f'Vis-{bar}-{y}',s*(x+7),y,11.9,3.4,8.3,'Z',[bar,front if y<201 else rear])
save('02-cassettes.json')

# Body grouping makes each full node selectable and movable as one assembly.
for side,ref in [('D','R'),('G','L')]:
 cmd('component.move_bodies',bodies=['BT-'+side,'BF-'+side,'HANDLE-'+side]+['REF_'+n+'_'+ref for n in ['TP2','MODULES','NVME','PSU','FAN']],component='CASSETTE-'+side)
cmd('component.activate',component='root')
save('03-groups.json')
