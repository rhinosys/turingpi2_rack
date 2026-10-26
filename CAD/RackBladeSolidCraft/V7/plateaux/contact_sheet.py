from pathlib import Path
import json,math
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).resolve().parent
reports=json.loads((P/'verification/audit-plateaux.json').read_text())
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',19)
small=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)
im=Image.new('RGB',(1600,1380),'#eef1f4');d=ImageDraw.Draw(im)
d.text((25,18),'V7 calibre — PETG HF noir / X1 Carbon / PEI lisse',font=font,fill='#172333')
for i,r in enumerate(reports):
 x=(i%4)*400;y=55+(i//4)*440
 d.rounded_rectangle((x+10,y,x+390,y+425),radius=14,fill='white')
 p=Image.open(P/(Path(r['file']).stem+'.png')).convert('RGBA');p.thumbnail((370,345))
 im.paste(p,(x+(400-p.width)//2,y+28),p)
 title=Path(r['file']).stem.replace('_',' ')
 if i==8:title='09 Façade D + poignée + biscuits'
 if i==9:title='10 Façade G + poignée + biscuits'
 if i==10:title='11 Option : tests de jonction'
 d.text((x+22,y+365),title[:34],font=small,fill='#172333')
 sec=int(r['slice']['prediction']);mass=float(r['slice']['weight'])
 d.text((x+22,y+393),f'{sec//3600} h {(sec%3600)//60:02d}  |  {mass:.0f} g',font=small,fill='#536577')
im.save(P/'Apercu_plateaux_V7.png')
