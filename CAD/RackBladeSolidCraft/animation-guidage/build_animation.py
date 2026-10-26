"""Animation pédagogique des maillages réels, sans modification de la CAO.
Coupe horizontale des parois pour exposer les deux guidages. Caméra fixe.
Le déplacement est imposé : ce rendu ne simule pas les contacts mécaniques.
"""
from pathlib import Path
import json, zipfile, math, xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT=Path(__file__).resolve().parent
ROOT=OUT.parent
NS={'m':'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
trans={x['name']:x for x in json.loads((ROOT/'verification/r1-2026-10-24/measure-print.json').read_text())}
trans.update({x['name']:x for x in json.loads((ROOT/'verification/print-changes.json').read_text())})
right=np.array([.81,.59,0.]); eye=np.array([.50,-.69,.72]);eye/=np.linalg.norm(eye)
up=np.cross(eye,right);up/=np.linalg.norm(up)
parts=[]
moving={'BT-D','BF-D','HANDLE-D'}

def clip(poly,zmax):
    result=[]
    for a,b in zip(poly,np.roll(poly,-1,axis=0)):
        ia,ib=a[2]<=zmax,b[2]<=zmax
        if ia:result.append(a)
        if ia!=ib:result.append(a+(b-a)*(zmax-a[2])/(b[2]-a[2]))
    return np.array(result)

for name in ['Q-AV-D','CL-AV','BT-G','BT-D','BF-D','HANDLE-D']:
    with zipfile.ZipFile(ROOT/f'exports/3mf/{name}.3mf') as z:
        r=ET.fromstring(z.read('3D/3dmodel.model'))
    v=np.array([[float(n.get(k)) for k in ['x','y','z']] for n in r.findall('.//m:vertex',NS)])
    f=np.array([[int(n.get(k)) for k in ['v1','v2','v3']] for n in r.findall('.//m:triangle',NS)])
    t=trans[name];a=np.array(t['axis']);ang=math.radians(t['angle'])
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    R=np.eye(3)*math.cos(ang)+(1-math.cos(ang))*np.outer(a,a)+math.sin(ang)*K
    v=(v-np.array(t['translate']))@R
    # Façade également coupée pour ne pas masquer l'entrée des rainures.
    limit=24 if name in {'CL-AV','Q-AV-D','BF-D'} else 1000
    base=np.array([36,166,157] if name in moving else ([230,159,55] if name=='CL-AV' else [146,163,181]))
    for tri in v[f]:
        normal=np.cross(tri[1]-tri[0],tri[2]-tri[0]);length=np.linalg.norm(normal)
        shade=.5+.5*abs(np.dot(normal/max(length,1e-9),[.35,-.4,.846]))
        p=clip(tri,limit)
        if len(p)>=3:parts.append((p,tuple((base*shade).astype(int)),name in moving))

W,H=1100,800
allp=np.concatenate([p for p,c,m in parts]+[p+[0,-220,0] for p,c,m in parts if m])
uv=np.column_stack([allp@right,allp@up]);lo=uv.min(0);hi=uv.max(0)
scale=min(960/(hi[0]-lo[0]),490/(hi[1]-lo[1]));mid=(hi+lo)/2
font='/System/Library/Fonts/Supplemental/Arial.ttf'
title=ImageFont.truetype(font,30);body=ImageFont.truetype(font,22);small=ImageFont.truetype(font,18)
def project(p):
    return np.column_stack([(p@right-mid[0])*scale+W/2,400-(p@up-mid[1])*scale])

def frame(distance,phase):
    im=Image.new('RGB',(W,H),'#f1f5f8');d=ImageDraw.Draw(im)
    polys=[]
    for p,c,m in parts:
        q=p+([0,-distance,0] if m else [0,0,0])
        polys.append((np.mean(q@eye),project(q),c))
    for _,p,c in sorted(polys,key=lambda x:x[0]):d.polygon([tuple(x) for x in p],fill=c)
    d.rectangle((0,0,W,98),fill='#172b42')
    d.text((30,17),'Comment le blade coulisse',font=title,fill='white')
    d.text((30,58),'Vue en coupe : dessus et haut des parois masqués',font=body,fill='#b7ccdd')
    d.rounded_rectangle((25,660,1075,778),radius=14,fill='white')
    for x,color,text in [(45,'#24a69d','Blade mobile'),(335,'#e69f37','Guide central'),(645,'#92a3b5','Châssis / autre tiroir')]:
        d.rectangle((x,679,x+18,697),fill=color);d.text((x+28,675),text,font=body,fill='#172b42')
    d.text((45,714),phase,font=body,fill='#172b42')
    d.text((45,746),'Les deux languettes suivent les rainures intérieure et extérieure.',font=small,fill='#52677b')
    d.text((30,110),f'Déplacement vers l’avant : {distance:.0f} mm',font=body,fill='#172b42')
    return im

sequence=[]
sequence += [(0,'1. En place : guidage des deux côtés.')]*12
for i in range(37):
    dist=220*(.5-.5*math.cos(math.pi*i/36))
    sequence.append((dist,'2. Extraction : tirer droit, en soutenant le tiroir.'))
sequence += [(220,'3. Sorti des rainures : le tiroir doit être soutenu.')]*18
for i in range(37):
    dist=220*(.5+.5*math.cos(math.pi*i/36))
    sequence.append((dist,'4. Réinsertion : aligner les deux languettes puis pousser.'))
sequence += [(0,'5. En place : remettre les fixations de façade.')]*12
frames=[frame(dist,phase) for dist,phase in sequence]
frames[0].save(OUT/'apercu.png')
frames[len(sequence)//2].save(OUT/'sortie.png')
frames[0].save(OUT/'Coulissement_Blade.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=False)
print('Animation créée :',len(frames),'images')
