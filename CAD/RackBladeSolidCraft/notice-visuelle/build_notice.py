from pathlib import Path
import json,zipfile,xml.etree.ElementTree as ET,math
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'notice-visuelle'; REPO=ROOT.parents[1]
PDF=REPO/'output/pdf/Notice_Rack_3D_V2.pdf'
N={'m':'http://schemas.microsoft.com/3dmanufacturing/core/2015/02'}
trans={x['name']:x for x in json.load(open(ROOT/'verification/r1-2026-10-24/measure-print.json'))}
trans.update({x['name']:x for x in json.load(open(ROOT/'verification/print-changes.json'))})
meshes={}
for name,t in trans.items():
 with zipfile.ZipFile(ROOT/f'exports/3mf/{name}.3mf') as z: r=ET.fromstring(z.read('3D/3dmodel.model'))
 v=np.array([[float(n.get(k)) for k in ['x','y','z']] for n in r.findall('.//m:vertex',N)])
 f=np.array([[int(n.get(k)) for k in ['v1','v2','v3']] for n in r.findall('.//m:triangle',N)])
 a=np.array(t['axis']); ang=math.radians(t['angle']); K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
 R=np.eye(3)*math.cos(ang)+(1-math.cos(ang))*np.outer(a,a)+math.sin(ang)*K
 world=(v-np.array(t['translate']))@R
 meshes[name]=(v,world,f)
# Exact exported triangles are projected orthographically; displacements are illustrative only.
right=np.array([.81,.59,0]); eye=np.array([.50,-.69,.52]); eye/=np.linalg.norm(eye); up=np.cross(eye,right);up/=np.linalg.norm(up)
font='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def render(filename, names, active=None, offsets=None, printview=False, badges=False):
 active=set(names if active is None else active);offsets=offsets or {}; W,H=1500,950
 polys=[];centers=[]
 for idx,name in enumerate(names):
  v0,v,f=meshes[name];v=(v0 if printview else v)+np.array(offsets.get(name,[0,0,0]))
  uv=np.column_stack([v@right,v@up]);depth=v@eye
  base=np.array([29,159,157] if name in active else [181,193,203])
  tri=v[f];norm=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);norm/=np.maximum(np.linalg.norm(norm,axis=1)[:,None],1e-9)
  shade=.50+.50*np.abs(norm@np.array([.35,-.4,.846]));cols=np.clip(base[None,:]*shade[:,None],0,255).astype(int)
  for face,c in zip(f,cols):polys.append((depth[face].mean(),uv[face],tuple(c)))
  centers.append((idx+1,name,uv.mean(axis=0)))
 alluv=np.concatenate([p[1] for p in polys]);lo=alluv.min(0);hi=alluv.max(0);scale=min((W-170)/(hi[0]-lo[0]),(H-150)/(hi[1]-lo[1]));mid=(hi+lo)/2
 def xy(q):return ((q[0]-mid[0])*scale+W/2,H/2-(q[1]-mid[1])*scale)
 im=Image.new('RGB',(W,H),'#f1f5f8');d=ImageDraw.Draw(im)
 for _,uv,c in sorted(polys,key=lambda p:p[0]):d.polygon([xy(q) for q in uv],fill=c)
 if offsets:
  for idx,name,q in centers:
   delta=np.array(offsets.get(name,[0,0,0]));length=np.linalg.norm(delta)
   if length<1:continue
   target=q-np.array([delta@right,delta@up]);start=np.array(xy(q));finish=np.array(xy(target));vec=finish-start;L=np.linalg.norm(vec)
   if L<40:continue
   u=vec/L;start=start+u*32
   d.line([tuple(start),tuple(finish)],fill='#e57b20',width=7)
   side=np.array([-u[1],u[0]])
   d.polygon([tuple(finish),tuple(finish-u*23+side*11),tuple(finish-u*23-side*11)],fill='#e57b20')
 if badges:
  ft=ImageFont.truetype(font,27)
  for idx,name,q in centers:
   if name not in active:continue
   x,y=xy(q);d.ellipse((x-24,y-24,x+24,y+24),fill='#172b42',outline='white',width=3);d.text((x,y),str(idx),font=ft,fill='white',anchor='mm')
 im.save(OUT/filename)
 return OUT/filename
Q=['Q-AV-G','Q-AV-D','Q-AR-G','Q-AR-D'];CL=['CL-AV','CL-AR'];FW=['FW-G','FW-D'];BT=['BT-G','BT-D'];BF=['BF-G','BF-D'];HA=['HANDLE-G','HANDLE-D'];EA=['EAR-G','EAR-D'];TOP=['TOP-AV-G','TOP-AV-D','TOP-AR-G','TOP-AR-D']
for name in trans:render('print-'+name+'.png',[name],printview=True)
render('quadrants.png',Q,offsets={n:[-35 if n.endswith('G') else 35,-30 if 'AV' in n else 30,0] for n in Q},badges=True)
render('cloisons.png',Q+CL,active=CL,offsets={n:[0,0,110] for n in CL},badges=True)
render('guidage.png',Q+CL+BT,active=BT,offsets={n:[0,-140,0] for n in BT},badges=True)
render('blade.png',['BT-D','BF-D','HANDLE-D'],offsets={'BF-D':[0,-45,0],'HANDLE-D':[0,-85,0]},badges=True)
render('ventilos.png',Q+CL+FW,active=FW,offsets={n:[0,0,90] for n in FW},badges=True)
render('oreilles.png',Q+CL+FW+BT+BF+HA+EA,active=EA,offsets={n:[-35 if n.endswith('G') else 35,-25,0] for n in EA},badges=True)
render('capots.png',Q+CL+FW+BT+BF+HA+EA+TOP,active=TOP,offsets={n:[-25 if n.endswith('G') else 25,-15 if 'AV' in n else 15,105] for n in TOP},badges=True)
render('final.png',Q+CL+FW+BT+BF+HA+EA+TOP,active=TOP)
W,H=842,595;c=canvas.Canvas(str(PDF),pagesize=(W,H));c.setTitle('Rack Blade - Notice visuelle 3D V2');page=0
style=ParagraphStyle('body',fontName='Helvetica',fontSize=11,leading=15,textColor=HexColor('#213449'))
small=ParagraphStyle('small',parent=style,fontSize=9,leading=12)
def p(txt,x,y,w=240,st=style):
 q=Paragraph(txt,st);_,h=q.wrap(w,800);q.drawOn(c,x,y-h);return y-h

def head(k,title,sub):
 global page
 page+=1;c.setFillColor(HexColor('#ffffff'));c.rect(0,0,W,H,fill=1,stroke=0)
 c.setFillColor(HexColor('#172b42'));c.rect(0,H-99,W,99,fill=1,stroke=0)
 c.setFillColor(HexColor('#58d5c3'));c.setFont('Helvetica-Bold',10);c.drawString(30,H-26,k)
 c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',23);c.drawString(30,H-56,title)
 c.setFont('Helvetica',10);c.drawString(30,H-78,sub)
 c.setStrokeColor(HexColor('#d6dfe7'));c.line(30,28,W-30,28)
 c.setFillColor(HexColor('#52677b'));c.setFont('Helvetica',8);c.drawString(30,15,'RACK BLADE / R3  •  NOTICE V2  •  25.10.2026  •  Prototype, interfaces à valider')
 c.drawRightString(W-30,15,str(page))
def img(path,x,y,w,h):c.drawImage(str(path),x,y,width=w,height=h,preserveAspectRatio=True,anchor='c',mask='auto')
def end():c.showPage()
def step(no,title,sub,im,parts,actions,check,note='Vue éclatée de présentation ; les écarts ne sont pas des cotes de montage.'):
 head('MONTAGE / '+no,title,sub);img(OUT/im,20,115,535,365)
 p(note,30,103,510,small);y=474
 y=p('<b>À préparer</b><br/>'+parts,575,y,235)-15
 for i,a in enumerate(actions,1):y=p(f'<b>{i}.</b> '+a,575,y,235)-10
 y=p('<b>Avant de continuer</b><br/>'+check,575,y-5,235)
 if y<38:raise ValueError((title,y))
 end()
head('GUIDE VISUEL / IMPRESSION + MONTAGE','Un rack, pièce par pièce','Deux baies Turing Pi 2.5 • PETG noir • X1 Carbon • Version de travail')
img(OUT/'final.png',20,75,535,400)
p('<b>Comment lire les vues</b><br/><br/>Turquoise : pièces ajoutées à l’étape.<br/>Gris : pièces déjà assemblées.<br/>Pastilles : numéros repris dans la liste de pièces.<br/>Flèches orange : sens de rapprochement.<br/><br/>Les couleurs sont uniquement pédagogiques : tout sera imprimé en noir.',580,470,230)
p('<b>Deux volets</b><br/>Pages 2-6 : repères et impression.<br/>Pages 7-15 : montage illustré.<br/>Page 16 : contrôles et suite.',580,270,230)
p('<b>Limite de cette V2</b><br/>Vues calculées depuis les vrais maillages R3. Visserie indicative ; fixation PSU et interfaces carte/SSD à relever. Ne pas lancer la série avant les essais de tolérances et la correction des faibles épaisseurs.',580,165,230,small);end()
for names,title in [(Q+CL+FW+BT,'Repérer le châssis et les tiroirs'),(BF+HA+EA+TOP,'Repérer la fermeture et les accessoires')]:
 head('COMPOSANTS / 1 EXEMPLAIRE PAR RÉFÉRENCE',title,'Les noms correspondent exactement aux fichiers 3MF. Ne pas mettre les pièces en miroir.')
 for i,n in enumerate(names):
  col=i%5;row=i//5;x=25+col*160;y=280-row*200
  img(OUT/('print-'+n+'.png'),x,y+24,150,165);c.setFillColor(HexColor('#172b42'));c.setFont('Helvetica-Bold',11);c.drawCentredString(x+75,y+13,n)
 end()
head('IMPRESSION / PROFIL COMMUN','Garder les mêmes réglages d’ajustement','La planche de tolérances constitue la référence de départ, pas une validation de résistance.')
img(ROOT/'Tolerances/Tolerance_top.png',25,120,485,355)
p('<b>Profil de la planche envoyée</b><br/>X1 Carbon, buse 0,4 mm.<br/>PETG HF noir, AMS A3.<br/>Plaque lisse.<br/>Couches 0,16 mm ; première 0,20 mm.<br/>XY trous / contours : 0 / 0 mm.<br/>Pied d’éléphant : 0,15 mm.<br/>Échelle 100 %, impression par couche.',550,470,260)
p('<b>Après refroidissement</b><br/>Tester écrous à plat et verticaux, biscuits et rainures. Retenir l’ajustement manuel sans fissure. Noter les valeurs dans resultats.csv.<br/><br/>J0.2 = jeu total de 0,2 mm.<br/>3.4 = hauteur de rainure de 3,4 mm.',550,295,260)
p('<b>Ne pas généraliser</b><br/>Les 2 parois et 15 % de remplissage sont ceux de la planche. Le profil structurel des grandes pièces reste à qualifier.',550,120,260,small);end()
for names,title,notes in [(['Q-AV-D','TOP-AV-D','BT-D','CL-AV'],'Les grandes pièces sur le plateau',['Fond en bas, paroi dressée. Examiner les ponts au-dessus des poches du dessous et les rails.','Face extérieure en bas. Reliefs vers le haut. Vérifier les ponts qui ferment les hexagones.','Orientation exportée. Examiner les nervures sous le fond et les logements sous entretoises.','Orientation exportée sur le flanc. Examiner les pieds en porte-à-faux et les logements.']),(['FW-D','BF-D','EAR-D','HANDLE-D'],'Les pièces secondaires sur le plateau',['Orientation exportée. Vérifier les pieds et le passage du ventilateur.','Face avant vers le plateau. Contrôler ouvertures, appuis et fixation du tiroir.','À plat. Les couches et le remplissage ne suffisent pas à qualifier la charge admissible.','Orientation exportée. Examiner le pont de la prise et les deux fixations.'])]:
 head('IMPRESSION / VUES DANS L’ORIENTATION DES 3MF',title,'Conserver l’orientation et l’échelle fournies ; inspecter le tranchage avant lancement.')
 for i,(n,note) in enumerate(zip(names,notes)):
  x=25+i*202;img(OUT/('print-'+n+'.png'),x,260,190,205)
  c.setFillColor(HexColor('#12a79d'));c.rect(x,255,190,3,fill=1,stroke=0)
  p('<b>'+n+'</b><br/>'+note,x,240,185)
 p('<b>Supports :</b> pas de support inaccessible dans un rail ou une poche d’écrou. L’impression sans support de toutes les pièces n’est pas validée. Corriger la géométrie ou revoir l’orientation si nécessaire.',30,103,780,small)
 p('Imprimer BIS / BIS-X à plat, 3 mm de haut. Le lot BIS_20_plus_BIS-X_2 contient 20 BIS + 2 BIS-X, dont 4 BIS de réserve.',30,60,780,small);end()
step('01','Présenter les quatre quadrants','Faire un premier montage à blanc sur une surface plane.','quadrants.png','1 Q-AV-G · 2 Q-AV-D<br/>3 Q-AR-G · 4 Q-AR-D<br/>Biscuits : voir page suivante.<br/>4 vis M4 × 16 + 4 écrous.',[
'Rapprocher les quatre pièces suivant cette vue, avant du rack vers le bas de l’image.',
'Préparer les écrous dans les pattes latérales avant de fermer les jonctions.',
'Approcher les 4 vis aux liaisons avant/arrière : 2 par côté. Ne pas bloquer.'],
'Fond à plat ; coutures fermées sans forcer. Aucun biscuit ne doit soulever une jonction.')
# Exact nominal biscuit layout, 8 + 1 per surface. Coordinates from design specification.
head('MONTAGE / 02','Positionner les biscuits de jonction','8 BIS + 1 BIS-X sous le fond ; même répartition sur les capots : 16 + 2 installés.')
x0,y0=70,88;s=.82
c.setFillColor(HexColor('#edf2f6'));c.rect(x0,y0,446*s,424*s,fill=1,stroke=0)
c.setStrokeColor(HexColor('#6c7c8b'));c.line(x0+223*s,y0,x0+223*s,y0+424*s);c.line(x0,y0+210*s,x0+446*s,y0+210*s)
pts=[(0,y) for y in [50,130,290,370]]+[(x,210) for x in [-160,-60,60,160]]
for i,(x,y) in enumerate(pts,1):
 xx=x0+(x+223)*s;yy=y0+y*s;c.setFillColor(HexColor('#0a9c96'));c.roundRect(xx-13,yy-9,26,18,3,fill=1,stroke=0);c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',9);c.drawCentredString(xx,yy-3,str(i))
xx=x0+223*s;yy=y0+210*s;c.setFillColor(HexColor('#172b42'));c.rect(xx-10,yy-10,20,20,fill=1,stroke=0);c.setFillColor(HexColor('#ffffff'));c.drawCentredString(xx,yy-3,'X')
c.setFillColor(HexColor('#172b42'));c.setFont('Helvetica-Bold',11);c.drawString(x0,65,'AVANT / Y = 0');c.drawString(x0,450,'ARRIÈRE / Y = 424')
p('<b>Carte de repérage des poches</b><br/>Schéma en plan, sans perspective. Les positions sont données dans le repère CAO ; suivre les poches réelles.',515,470,290)
img(OUT/'print-BIS.png',515,280,130,100);img(OUT/'print-BIS-X.png',665,280,130,100)
p('<b>BIS</b> : rectangulaire 21,8 × 19,8 × 3 mm.<br/><b>BIS-X</b> : carré 21,8 × 21,8 × 3 mm.<br/><br/>Sous le fond : retourner le châssis vide en le soutenant. Engager les biscuits à cheval sur les coutures, sans colle pour l’essai. Reposer à plat avant de poursuivre.<br/><br/>Sur les capots : poser après présentation des quatre panneaux. Vérifier l’affleurement.',515,275,290)
end()
step('03','Descendre les deux cloisons','Les cloisons relient les deux moitiés du plancher.','cloisons.png','5 CL-AV · 6 CL-AR<br/>16 vis M4 × 12 + écrous.',[
'Placer les écrous côté pattes, avant que leur accès ne soit masqué.',
'Présenter CL-AV au centre de la zone avant : ses deux rainures doivent faire face aux rails extérieurs.',
'Présenter CL-AR à l’arrière ; approcher les vis depuis le dessous, châssis vide et soutenu.'],
'Pieds en appui, cloisons droites. Contrôler le dégagement de 0,2 mm sous CL-AR ; caler si nécessaire.')
step('04','Essayer les tiroirs sans électronique','Tester toute la course avant de monter les équipements.','guidage.png','7 BT-G · 8 BT-D<br/>Aucune vis pour le coulissement.',[
'Aligner simultanément les deux langues de chaque tiroir avec les rainures intérieure et extérieure.',
'Engager depuis l’avant et pousser doucement. Ne pas engager un seul côté en biais.',
'Effectuer plusieurs sorties/entrées complètes ; localiser toute zone qui coince.'],
'Aucun point dur. Les 195 mm simulés ne qualifient pas le frottement ni le parallélisme réels.')
step('05','Assembler une façade de blade','Répéter avec les références G pour l’autre tiroir.','blade.png','1 BT-D · 2 BF-D · 3 HANDLE-D<br/>Par blade : 4 M3 × 12 + écrous ; 2 M4 × 35 + écrous.',[
'Présenter BF-D contre le chant avant de BT-D. Aligner les quatre passages M3.',
'Placer les écrous dans leurs logements accessibles ; approcher les vis M3.',
'Fixer la poignée sur ses deux points M4. Contrôler engagement des vis, puis serrer progressivement.'],
'Façade plaquée sans cintrage. Les vis ne doivent pas gêner les rails ou la future carte.')
step('06','Installer les supports de ventilation','Les ventilateurs doivent souffler vers les alimentations, à l’arrière.','ventilos.png','7 FW-G · 8 FW-D<br/>4 M4 × 16 + écrous pour les pieds.<br/>8 M4 × 35 + écrous pour les 2 ventilateurs.',[
'Descendre les deux parois dans leur position derrière les tiroirs ; fixer les pieds au plancher.',
'Présenter chaque ventilateur 120 × 120 × 25 contre sa paroi. Aligner les quatre trous.',
'Orienter la flèche de débit vers l’arrière ; placer les écrous côté ventilateur et serrer sans déformer.'],
'Pales libres. Aucun fil dans le passage d’air. Les volumes ventilateurs ne sont pas dessinés sur cette vue.')
head('MONTAGE / 07','Présenter le matériel et les câbles','Montage hors tension. Les volumes transparents sont des enveloppes, pas les équipements exacts.')
img(ROOT/'previews/assembly-open.png',20,120,540,355)
p('<b>Par baie</b><br/>1 TP2.5 + 4 RK1 ventilés.<br/>4 vis M3 × 22 + écrous sous les entretoises.<br/>1 alimentation + sangle.',575,470,235)
p('<b>1.</b> Vérifier les trous de carte, ports de façade, dégagement SSD et longueur de vis avant de fixer.<br/><br/><b>2.</b> Poser l’alimentation dans son berceau. Relever les trous UNC 6-32 : ils sont absents du modèle actuel.<br/><br/><b>3.</b> Router l’ATX hors rails et pales. Prévoir la réserve mobile puis tester le tiroir hors tension.',575,365,235)
p('<b>Arrêt avant montage définitif</b><br/>Fixation PSU, interface I/O et accès SSD non validés. Ne pas forcer une carte pour rattraper un mauvais alignement.',30,100,770,small);end()
step('08','Fixer les oreilles, vérifier le verrouillage','La baie doit soutenir le châssis par-dessous pendant les essais.','oreilles.png','15 EAR-G · 16 EAR-D<br/>6 M4 × 12 + écrous.<br/>4 M4 moletées × 12 pour les blades.',[
'Présenter chaque oreille contre le cadre avant : trois points M4 par oreille.',
'Approcher puis serrer les vis. Vérifier que les façades passent entre les oreilles.',
'Fermer les deux tiroirs et essayer leurs deux vis moletées chacun, sans forcer l’alignement.'],
'Les poignées servent aux tiroirs. La résistance des oreilles et du châssis chargé reste à qualifier.')
step('09','Fermer avec les quatre capots','L’air doit entrer devant et ressortir derrière.','capots.png','17 TOP-AV-G · 18 TOP-AV-D<br/>19 TOP-AR-G · 20 TOP-AR-D<br/>12 M4 × 12 ; 4 M4 × 16 + rondelles larges ; écrous.',[
'Poser les joints fins aux coutures, sans obstruer les grilles avant et arrière.',
'Descendre les capots, présenter leurs biscuits (page 8), puis approcher les vis des rabats.',
'Poser les fixations centrales avec rondelles sur la couture ; serrer progressivement sans déformer.'],
'Fonds hexagonaux intacts, joints comprimés, aucun câble pincé. Ne jamais déboucher les alvéoles.')
head('CONTRÔLES / VERSION SUIVANTE','Valider avant la fabrication complète','Cette notice propose une séquence ; les essais physiques restent nécessaires.')
img(OUT/'final.png',25,130,480,345)
p('<b>Réception du montage</b><br/>[ ] Fond plat, assemblages sans fissures.<br/>[ ] Tiroirs libres et verrouillables.<br/>[ ] Cartes et PSU correctement retenues.<br/>[ ] Vis sans contact avec l’électronique.<br/>[ ] Câbles libres sur toute la course.<br/>[ ] Aspiration avant, rejet arrière.<br/>[ ] Essai thermique progressif et relevé des températures.',540,470,265)
p('<b>À corriger / confirmer</b><br/>Jeux issus de la planche ; nervures de tiroir de 1,6 mm ; résidu de 0,4 mm sous certaines poches M3 ; interfaces PSU, I/O et SSD ; profils et supports par pièce ; charge admissible du rack.',540,260,265)
p('<b>Sources et portée</b><br/>Maillages exports/3mf R3 ; transformations de measure-print.json et print-changes.json ; BOM.md ; rapports R1/R3 ; notice V1. Les vues éclatées sont des déplacements de présentation. Aucun nouveau fichier de pièce ni aucune impression n’a été lancé.',30,102,775,small)
end();c.save();print(PDF);print('Pages:',page)
