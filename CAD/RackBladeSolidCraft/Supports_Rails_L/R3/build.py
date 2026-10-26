"""Four PETG end saddles for user-cut L15.5 rails. Native SolidCraft MCP build."""
from pathlib import Path
import json,subprocess,math
P=Path(__file__).resolve().parent
cmd=[]
# Field fit correction: metal hole centres reported at 15, 35, 50 mm.
# Select 35 mm, preserving the end stop at y=18.
RAIL_HOLE_FROM_END=35
M4_Y=18+RAIL_HOLE_FROM_END
def add(c,**p):cmd.append(dict(command=c,params=p))
for n,v in dict(m6_d=6.8,m4_d=4.3,m4_nut_af=7.2).items():add('parameters.change',name=n,expression=v)
for body,sign,offset in [('AV-A',1,0),('AV-B',-1,100),('AR-A',1,200),('AR-B',-1,300)]:
 def box(n,x,y,z,l,w,h,op='join'):
  xx=offset+x if sign==1 else offset-x-l
  add('solid.box',name=body+'-'+n,body_name=body if op=='new' else None,corner=[xx,y,z],length=l,width=w,height=h,operation=op,**({} if op=='new' else dict(targets=[body])))
 box('Platine',-15,0,0,30,8,56,'new')
 box('Tablette',-15,0 if body.startswith('AR-') else 7.8,24,44,61 if body.startswith('AR-') else 48.2,8)
 for x,t in [(-15,4),(11,4)]:
  add('sketch.create',plane=dict(origin=[offset+sign*x,0,0],x_dir=[0,1,0],y_dir=[0,0,1]),name=body+'-Nervure')
  add('sketch.line',points=[[7.8,4],[61 if body.startswith('AR-') else 56,24],[61 if body.startswith('AR-') else 56,24.1],[7.8,24.1]],closed=True)
  add('sketch.finish')
  add('solid.extrude',distance=t,direction='positive' if sign==1 else 'negative',operation='join',targets=[body],name=body+'-Renfort')
 # Channel 16.1 mm, offset inward. Lips lower than the 1.5 mm steel flange.
 box('Bord-exterieur',-15,8,31.9,18.7,53 if body.startswith('AR-') else 48,1.1)
 box('Bord-interieur',19.8,8,31.9,9.2,53 if body.startswith('AR-') else 48,1.1)
 box('Butee',3.7,16,31.9,16.1,2,2.1)
 # Rear only: pocket around the horizontal wing, leaving the vertical wing free.
 if body.startswith('AR-'):
  box('Paroi-gorge',19.8,18,32,4.2,41,8.1)
  box('Toit-gorge',5.9,18,34.1,18.1,41,6)
  # Back ramp rises less than 45 degrees when the mounting face is on the bed.
  add('sketch.create',plane=dict(origin=[offset+sign*5.9,0,0],x_dir=[0,1,0],y_dir=[0,0,1]),name=body+'-Rampe-gorge')
  add('sketch.line',points=[[8,31.9],[18,31.9],[18,40.1]],closed=True)
  add('sketch.finish')
  add('solid.extrude',distance=18.1,direction='positive' if sign==1 else 'negative',operation='join',targets=[body],name=body+'-Fond-gorge-renforce')
  cx=offset+sign*11.75
  # Clear the thin tip of the lower rib so an M4 head and driver reach the shelf.
  add('solid.cylinder',radius=5,height=24.1,base=[cx,M4_Y,-0.1],axis=[0,0,1],operation='cut',targets=[body],name=body+'-Acces-tete-M4')
  add('solid.cylinder',radius='m4_d/2',height=18,base=[cx,M4_Y,23],axis=[0,0,1],operation='cut',targets=[body],name=body+'-Passage-M4')
  # Flat-to-flat 7.2, top-open pocket, 3.4 mm deep, floor retained below nut.
  add('sketch.create',plane=dict(origin=[0,0,36.7],x_dir=[1,0,0],y_dir=[0,1,0]),name=body+'-Ecrou-M4')
  add('sketch.line',points=[[cx+7.2/math.sqrt(3)*math.cos(math.radians(a)),M4_Y+7.2/math.sqrt(3)*math.sin(math.radians(a))] for a in [30,90,150,210,270,330]],closed=True)
  add('sketch.finish')
  add('solid.extrude',distance=3.5,operation='cut',targets=[body],name=body+'-Logement-ecrou-M4')
 # Two vertical oblongs: 6.8 x 10.8, centred 31.75 apart.
 for z in [12,43.75]:
  box('Lumiere',-3.4,-1,z-2,6.8,10,4,'cut')
  for zz in [z-2,z+2]:add('solid.cylinder',radius='m6_d/2',height=10,base=[offset,-1,zz],axis=[0,1,0],operation='cut',targets=[body],name=body+'-M6')
(P/'commands.json').write_text(json.dumps(cmd,indent=2))
proc=subprocess.Popen(['/Applications/SolidCraft.app/Contents/MacOS/solidcraft-cli','mcp','--headless','--allow-path',str(P)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
seq=0
def rpc(method,params):
 global seq
 seq+=1;proc.stdin.write(json.dumps(dict(jsonrpc='2.0',id=seq,method=method,params=params))+'\n');proc.stdin.flush()
 while True:
  line=proc.stdout.readline()
  if not line:raise RuntimeError('MCP closed')
  r=json.loads(line)
  if r.get('id')==seq:return r
rpc('initialize',dict(protocolVersion='2024-11-05',capabilities={},clientInfo=dict(name='rail-saddles',version='1')))
proc.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n');proc.stdin.flush()
def call(label,name,args):
 r=rpc('tools/call',dict(name=name,arguments=args));(P/'verification'/f'{label}.json').write_text(json.dumps(r,indent=2))
 if r.get('error') or r.get('result',{}).get('isError'):raise RuntimeError(r)
 d=json.loads(r['result']['content'][0]['text'])
 if isinstance(d,dict) and d.get('ok') is False:raise RuntimeError(d)
 print(label,str(d)[:160],flush=True);return d
try:
 call('new','new_design',dict(name='Supports_Rails_L_PETG_R3'))
 call('build','batch',dict(commands=cmd,verbose=False,rollback=True))
 call('inspect','inspect_design',dict(measure=False,sketches=False,joints=False))
 m=call('measure','measure',{})
 assert len(m['bodies'])==4 and all(b['kernel']['shells']==1 for b in m['bodies'])
 call('save','save',dict(path=str(P/'Supports_Rails_L_PETG_R3.solidcraft')))
 call('step','export',dict(path=str(P/'exports/Supports_Rails_L.step'),format='step'))
 # Short steel references explain the seat; their length is illustrative only.
 refs=[]
 for n,x in [('REF-L-A',204),('REF-L-B',280.5)]:
  refs += [dict(command='solid.box',params=dict(name=n,body_name=n,corner=[x,18,32],length=15.5,width=82,height=1.5,operation='new'))]
  vx=x if n.endswith('A') else x+14
  refs += [dict(command='solid.box',params=dict(name=n+'-aile',corner=[vx,18,32],length=1.5,width=82,height=15.5,operation='join',targets=[n]))]
  cx=211.75 if n.endswith('A') else 288.25
  refs += [dict(command='solid.cylinder',params=dict(name=n+'-Percage-M4',radius=2.15,height=3,base=[cx,M4_Y,31.5],axis=[0,0,1],operation='cut',targets=[n]))]
 # Schematic metal screws and nuts; excluded from every printing export.
 for side,cx in [('A',211.75),('B',288.25)]:
  bolt='REF-VIS-M4-'+side;nut='REF-ECROU-M4-'+side
  refs += [dict(command='solid.cylinder',params=dict(name=bolt,body_name=bolt,radius=3.5,height=4,base=[cx,M4_Y,20],operation='new')),
           dict(command='solid.cylinder',params=dict(name=bolt+'-tige',radius=2,height=20.1,base=[cx,M4_Y,23.9],operation='join',targets=[bolt])),
           dict(command='sketch.create',params=dict(plane=dict(origin=[0,0,36.7],x_dir=[1,0,0],y_dir=[0,1,0]),name=nut+'-profil')),
           dict(command='sketch.line',params=dict(points=[[cx+7/math.sqrt(3)*math.cos(math.radians(a)),M4_Y+7/math.sqrt(3)*math.sin(math.radians(a))] for a in [30,90,150,210,270,330]],closed=True)),
           dict(command='sketch.finish',params={}),
           dict(command='solid.extrude',params=dict(name=nut,body_name=nut,distance=3.2,operation='new')),
           dict(command='solid.cylinder',params=dict(name=nut+'-filetage-simplifie',radius=2.1,height=4,base=[cx,M4_Y,36.5],operation='cut',targets=[nut]))]
 call('reference-rails' ,'batch',dict(commands=refs,verbose=False))
 call('interference','execute',dict(command='inspect.interference',params=dict(budget_s=45),verbose=False))
 call('demo-save','save',dict(path=str(P/'Montage_berceaux_reference.solidcraft')))
 call('demo-step','export',dict(path=str(P/'exports/Montage_berceaux_reference.step'),format='step',bodies=['AR-A','AR-B','REF-L-A','REF-L-B','REF-VIS-M4-A','REF-VIS-M4-B','REF-ECROU-M4-A','REF-ECROU-M4-B']))
 # Lay outer rib faces on the bed, so the plate, shelf and lower gusset start together.
 call('orient','batch',dict(commands=[dict(command='solid.move',params=dict(bodies=[n],axis=[1,0,0] if n.startswith('AR-') else [0,1,0],angle=90 if n.startswith('AR-') else (-90 if n.endswith('A') else 90))) for n in ['AV-A','AV-B','AR-A','AR-B']],verbose=False))
 m=call('measure-rotated','measure',{})
 call('normalize','batch',dict(commands=[dict(command='solid.move',params=dict(bodies=[b['name']],translate=[-v for v in b['bbox']['min']])) for b in m['bodies'] if b['name'].startswith(('AV-','AR-'))],verbose=False))
 for n in ['AV-A','AV-B','AR-A','AR-B']:
  for fmt in ['3mf','step']:call(n+'-'+fmt,'export',dict(path=str(P/'exports'/f'{n}.{fmt}'),format=fmt,bodies=[n]))
finally:proc.terminate()
