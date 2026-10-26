"""Build one Bambu Studio project per plate; never sends a print job.
Meshes are calibrated, normalized V7 exports. The tested process/filament is
preserved; support and adhesion are explicit plate preparation choices.
"""
from pathlib import Path
import json,zipfile,xml.etree.ElementTree as E,copy,subprocess,sys
P=Path(__file__).resolve().parent
(P/'sources').mkdir(exist_ok=True)
(P/'verification').mkdir(exist_ok=True)
N='http://schemas.microsoft.com/3dmanufacturing/core/2015/02'
T=lambda x:'{'+N+'}'+x
E.register_namespace('',N)
CLI='/Applications/BambuStudio.app/Contents/MacOS/BambuStudio'
plates=[]
def plate(label,items,support=True):plates.append(dict(name=label,items=items,support=support))
for i,n in enumerate(['Q-AV-D','Q-AV-G-EAR','Q-AR-D','Q-AR-G','BT-D','FOND-AR-D','BT-G','FOND-AR-G'],1):plate(f'{i:02d}_{n}',[(n,None,20 if n.startswith('FOND-AR') else None)])
for i,side in [(9,'D'),(10,'G')]:
 items=[('BF-'+side,24.5,18),('HANDLE-'+side,25,195)]
 items += [('BIS',125+j*29,195) for j in range(4)]
 items += [('BIS',25+j*29,228) for j in range(4)]
 items += [('BIS-X',141,228)]
 plate(f'{i:02d}_Facade_{side}_poignee_biscuits',items,False)
plate('11_OPTION_Test_filament_et_jonction',[('TEST-FILAMENT',35,105),('TEST-JONCTION',145,105)])
(P/'inventaire.json').write_text(json.dumps(plates,indent=2))

def run(args,log):
 with open(log,'w') as f:r=subprocess.run([CLI]+args,stdout=f,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError(f'Bambu exit {r.returncode}: {log}')

for pl in plates:
 if len(sys.argv)>1 and pl['name'].split('_')[0] not in sys.argv[1:]:continue
 name=pl['name'];root=E.Element(T('model'),{'unit':'millimeter'})
 res=E.SubElement(root,T('resources'));build=E.SubElement(root,T('build'));oid=0;bounds=[]
 for ref,x,y in pl['items']:
  with zipfile.ZipFile(P.parent/'exports'/f'{ref}.3mf') as z:
   template={n:z.read(n) for n in z.namelist()};src=E.fromstring(template['3D/3dmodel.model'])
  meshes=src.findall('.//'+T('mesh'))
  allv=[tuple(float(v.get(k)) for k in ['x','y','z']) for m in meshes for v in m.find(T('vertices'))]
  lo=[min(v[a] for v in allv) for a in range(3)];hi=[max(v[a] for v in allv) for a in range(3)]
  dx=hi[0]-lo[0];dy=hi[1]-lo[1]
  if x is None:x=(256-dx)/2
  if y is None:y=(256-dy)/2
  assert x>=0 and y>=0 and x+dx<=256.001 and y+dy<=256.001 and hi[2]-lo[2]<=250
  assert x>=18 or y>=28,'forbidden region'
  for j,m in enumerate(meshes):
   oid+=1;obj=E.SubElement(res,T('object'),{'id':str(oid),'type':'model','name':ref+(f'-{j+1}' if len(meshes)>1 else '')})
   m=copy.deepcopy(m)
   for v in m.find(T('vertices')):
    for a,k in enumerate(['x','y','z']):v.set(k,format(float(v.get(k))-lo[a]+[x,y,0][a],'.10g'))
   obj.append(m);E.SubElement(build,T('item'),{'objectid':str(oid)})
  bounds.append(dict(part=ref,min=[x,y,0],max=[x+dx,y+dy,hi[2]-lo[2]]))
 for a in range(len(bounds)):
  for b in range(a):
   A,B=bounds[a],bounds[b]
   assert any(A['min'][k]>=B['max'][k] or B['min'][k]>=A['max'][k] for k in [0,1]),(A,B)
 raw=P/'sources'/f'{name}_geometrie.3mf'
 with zipfile.ZipFile(raw,'w',zipfile.ZIP_DEFLATED) as z:
  for n in ['[Content_Types].xml','_rels/.rels']:z.writestr(n,template[n])
  z.writestr('3D/3dmodel.model',E.tostring(root,encoding='utf-8',xml_declaration=True))
 run(['--arrange','0','--orient','0','--export-3mf',name+'_bambu.3mf','--outputdir',str(P/'sources'),str(raw)],P/'verification'/f'{name}_import.log')
 intermediate=P/'sources'/f'{name}_bambu.3mf'
 cfg=json.loads((P/'profil_PETG_HF_noir_X1C.json').read_text())
 cfg.update(enable_support='1' if pl['support'] else '0',support_type='normal(auto)',support_style='snug',support_on_build_plate_only='0',bridge_no_support='1',brim_type='outer_only' if name[:2] in ['01','02','03','04'] else 'auto_brim')
 with zipfile.ZipFile(intermediate) as src:contents={n:src.read(n) for n in src.namelist()}
 contents['Metadata/project_settings.config']=json.dumps(cfg,indent=2).encode()
 # The initial generic import has no machine profile and does not assign
 # objects to a plate. Explicitly assign every object to this single plate.
 ms=E.fromstring(contents['Metadata/model_settings.config']);plat=ms.find('plate')
 for inst in list(plat.findall('model_instance')):plat.remove(inst)
 for ob in ms.findall('object'):
  inst=E.SubElement(plat,'model_instance')
  for k,v in [('object_id',ob.get('id')),('instance_id','0'),('identify_id',ob.get('id'))]:E.SubElement(inst,'metadata',{'key':k,'value':v})
 contents['Metadata/model_settings.config']=E.tostring(ms,encoding='utf-8',xml_declaration=True)
 with zipfile.ZipFile(P/f'{name}.3mf','w',zipfile.ZIP_DEFLATED) as z:
  for n,data in contents.items():z.writestr(n,data)
 (P/'verification'/f'{name}_placement.json').write_text(json.dumps(bounds,indent=2))
 print(name,'prepared',flush=True)
