from pathlib import Path
import zipfile,json,xml.etree.ElementTree as E,copy,subprocess,shutil,io,sys
from PIL import Image
P=Path(__file__).resolve().parent;N='http://schemas.microsoft.com/3dmanufacturing/core/2015/02';T=lambda n:'{'+N+'}'+n
E.register_namespace('',N)
root=E.Element(T('model'),{'unit':'millimeter'});res=E.SubElement(root,T('resources'));build=E.SubElement(root,T('build'))
placements=[]
full='--complet' in sys.argv
plate_name='Plateau_4_supports_R3' if full else 'Plateau_2_arriere_M4_R3'
layout=[('AV-A',45,45),('AV-B',145,45),('AR-A',45,145),('AR-B',145,145)] if full else [('AR-A',60,100),('AR-B',150,100)]
for i,(name,x,y) in enumerate(layout,1):
 with zipfile.ZipFile(P/'exports'/f'{name}.3mf') as z:
  template={n:z.read(n) for n in z.namelist()};tree=E.fromstring(template['3D/3dmodel.model'])
 m=copy.deepcopy(tree.find('.//'+T('mesh')))
 for v in m.find(T('vertices')):v.set('x',str(float(v.get('x'))+x));v.set('y',str(float(v.get('y'))+y))
 ob=E.SubElement(res,T('object'),{'id':str(i),'type':'model','name':f'{name}-{i}'});ob.append(m);E.SubElement(build,T('item'),{'objectid':str(i)})
 placements.append(dict(name=name,x=x,y=y))
raw=P/'verification/geometrie_plateau.3mf'
with zipfile.ZipFile(raw,'w',zipfile.ZIP_DEFLATED) as z:
 for n in ['[Content_Types].xml','_rels/.rels']:z.writestr(n,template[n])
 z.writestr('3D/3dmodel.model',E.tostring(root,encoding='utf-8',xml_declaration=True))
CLI='/Applications/BambuStudio.app/Contents/MacOS/BambuStudio'
def run(args,log):
 with (P/'verification'/log).open('w') as f:subprocess.run([CLI]+args,stdout=f,stderr=subprocess.STDOUT,check=True)
run(['--arrange','0','--orient','0','--export-3mf','bambu_initial.3mf','--outputdir',str(P/'verification'),str(raw)],'import.log')
with zipfile.ZipFile(P/'verification/bambu_initial.3mf') as z:entries={n:z.read(n) for n in z.namelist()}
cfg=json.loads((P.parents[1]/'V7/plateaux/profil_PETG_HF_noir_X1C.json').read_text())
cfg.update(layer_height='0.2',wall_loops='6',sparse_infill_density='40%',sparse_infill_pattern='gyroid',top_shell_layers='6',bottom_shell_layers='6',enable_support='0',brim_type='outer_only',brim_width='5',print_settings_id='Berceaux PETG - 0.20 - 6 parois - 40%')
entries['Metadata/project_settings.config']=json.dumps(cfg,indent=2).encode()
ms=E.fromstring(entries['Metadata/model_settings.config']);plate=ms.find('plate')
for inst in list(plate.findall('model_instance')):plate.remove(inst)
for ob in ms.findall('object'):
 inst=E.SubElement(plate,'model_instance')
 for k,v in [('object_id',ob.get('id')),('instance_id','0'),('identify_id',ob.get('id'))]:E.SubElement(inst,'metadata',{'key':k,'value':v})
entries['Metadata/model_settings.config']=E.tostring(ms,encoding='utf-8',xml_declaration=True)
out=P/(plate_name+'_PETG_noir.3mf')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n,d in entries.items():z.writestr(n,d)
run(['--arrange','0','--orient','0','--slice','1','--export-3mf',out.name,'--outputdir',str(P/'verification'),str(out)],'slice.log')
shutil.copy2(P/'verification'/out.name,out)
run(['--arrange','0','--orient','0','--export-png','1','--outputdir',str(P/'verification'),str(out)],'preview.log')
shutil.copy2(P/'verification/plate_1_0.png',P/(plate_name+'.png'))
with zipfile.ZipFile(out) as z:entries={n:z.read(n) for n in z.namelist()}
entries['Metadata/plate_1.png']=(P/(plate_name+'.png')).read_bytes()
# This optional CLI statistic can be uninitialised; mark it unavailable rather than publish a negative time.
si=E.fromstring(entries['Metadata/slice_info.config'])
md={m.get('key'):m.get('value') for m in si.findall('./plate/metadata')}
for m in si.findall('./plate/metadata'):
 if m.get('key')=='first_layer_time' and (float(m.get('value'))<0 or float(m.get('value'))>float(md['prediction'])):m.set('value','0.000000')
entries['Metadata/slice_info.config']=E.tostring(si,encoding='utf-8',xml_declaration=True)

with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n,d in entries.items():z.writestr(n,d)
info=E.fromstring(entries['Metadata/slice_info.config']);meta={m.get('key'):m.get('value') for m in info.findall('./plate/metadata')}
assert meta['outside']=='false' and len(info.findall('./plate/object'))==len(layout)
assert all(x.get('skipped')=='false' for x in info.findall('./plate/object'))
assert len(info.findall('./plate/filament'))==1
fp=json.loads(entries['Metadata/plate_1.json'])['bbox_all'];assert min(fp)>28 and max(fp)<256
(P/('verification/'+plate_name+'.json')).write_text(json.dumps(dict(placement=placements,slice=meta,first_layer_bbox_with_brim=fp),indent=2))
print(meta)
