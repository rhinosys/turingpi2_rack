"""Four PETG end saddles for user-cut L15.5 rails. Native SolidCraft MCP build."""
from pathlib import Path
import json,subprocess
P=Path(__file__).resolve().parent
cmd=[]
def add(c,**p):cmd.append(dict(command=c,params=p))
for n,v in dict(m6_d=6.8).items():add('parameters.change',name=n,expression=v)
for body,sign,offset in [('BERCEAU-A',1,0),('BERCEAU-B',-1,100)]:
 def box(n,x,y,z,l,w,h,op='join'):
  xx=offset+x if sign==1 else offset-x-l
  add('solid.box',name=body+'-'+n,body_name=body if op=='new' else None,corner=[xx,y,z],length=l,width=w,height=h,operation=op,**({} if op=='new' else dict(targets=[body])))
 box('Platine',-15,0,0,30,8,56,'new')
 box('Tablette',-15,7.8,24,44,48.2,8)
 for x,t in [(-15,4),(11,4)]:
  add('sketch.create',plane=dict(origin=[offset+sign*x,0,0],x_dir=[0,1,0],y_dir=[0,0,1]),name=body+'-Nervure')
  add('sketch.line',points=[[7.8,4],[56,24],[56,24.1],[7.8,24.1]],closed=True)
  add('sketch.finish')
  add('solid.extrude',distance=t,direction='positive' if sign==1 else 'negative',operation='join',targets=[body],name=body+'-Renfort')
 # Channel 16.1 mm, offset inward. Lips lower than the 1.5 mm steel flange.
 box('Bord-exterieur',-15,8,31.9,18.7,48,1.1)
 box('Bord-interieur',19.8,8,31.9,9.2,48,1.1)
 box('Butee',3.7,16,31.9,16.1,2,2.1)
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
 call('new','new_design',dict(name='Supports_Rails_L_PETG_R1'))
 call('build','batch',dict(commands=cmd,verbose=False,rollback=True))
 call('inspect','inspect_design',dict(measure=False,sketches=False,joints=False))
 m=call('measure','measure',{})
 assert len(m['bodies'])==2 and all(b['kernel']['shells']==1 for b in m['bodies'])
 call('save','save',dict(path=str(P/'Supports_Rails_L_PETG_R1.solidcraft')))
 call('step','export',dict(path=str(P/'exports/Supports_Rails_L.step'),format='step'))
 # Short steel references explain the seat; their length is illustrative only.
 refs=[]
 for n,x in [('REF-L-A',4),('REF-L-B',80.5)]:
  refs += [dict(command='solid.box',params=dict(name=n,body_name=n,corner=[x,18,32],length=15.5,width=82,height=1.5,operation='new'))]
  vx=x if n.endswith('A') else x+14
  refs += [dict(command='solid.box',params=dict(name=n+'-aile',corner=[vx,18,32],length=1.5,width=82,height=15.5,operation='join',targets=[n]))]
 call('reference-rails','batch',dict(commands=refs,verbose=False))
 call('demo-save','save',dict(path=str(P/'Montage_berceaux_reference.solidcraft')))
 call('demo-step','export',dict(path=str(P/'exports/Montage_berceaux_reference.step'),format='step'))
 # Lay outer rib faces on the bed, so the plate, shelf and lower gusset start together.
 call('orient','batch',dict(commands=[dict(command='solid.move',params=dict(bodies=[n],axis=[0,1,0],angle=-90 if n=='BERCEAU-A' else 90)) for n in ['BERCEAU-A','BERCEAU-B']],verbose=False))
 m=call('measure-rotated','measure',{})
 call('normalize','batch',dict(commands=[dict(command='solid.move',params=dict(bodies=[b['name']],translate=[-v for v in b['bbox']['min']])) for b in m['bodies'] if b['name'].startswith('BERCEAU')],verbose=False))
 for n in ['BERCEAU-A','BERCEAU-B']:
  for fmt in ['3mf','step']:call(n+'-'+fmt,'export',dict(path=str(P/'exports'/f'{n}.{fmt}'),format=fmt,bodies=[n]))
finally:proc.terminate()
