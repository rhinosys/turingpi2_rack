"""Local slicing verification. Output stays on disk; no printer/network action."""
from pathlib import Path
import subprocess,sys,shutil,zipfile,json
P=Path(__file__).resolve().parent
CLI='/Applications/BambuStudio.app/Contents/MacOS/BambuStudio'
for f in sorted(P.glob('[0-9][0-9]_*.3mf')):
 if len(sys.argv)>1 and f.name[:2] not in sys.argv[1:]:continue
 out=P/'verification'/f.stem;out.mkdir(exist_ok=True)
 with (out/'bambu.log').open('w') as log:
  r=subprocess.run([CLI,'--arrange','0','--orient','0','--slice','1','--export-3mf',f.name,'--outputdir',str(out),str(f)],stdout=log,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError((f,r.returncode))
 result=out/f.name
 with zipfile.ZipFile(result) as z:
  assert 'Metadata/plate_1.gcode' in z.namelist()
 shutil.copy2(result,f)
 with (out/'preview.log').open('w') as log:
  subprocess.run([CLI,'--arrange','0','--orient','0','--export-png','1','--outputdir',str(out),str(f)],stdout=log,stderr=subprocess.STDOUT,check=True)
 if (out/'plate_1_0.png').exists():shutil.copy2(out/'plate_1_0.png',P/(f.stem+'.png'))
 # Embed the freshly rendered model preview instead of a blank headless thumbnail.
 if (out/'plate_1_0.png').exists():
  from PIL import Image
  import io
  with zipfile.ZipFile(f) as z:entries={n:z.read(n) for n in z.namelist()}
  preview=(out/'plate_1_0.png').read_bytes()
  entries['Metadata/plate_1.png']=preview
  entries['Metadata/plate_no_light_1.png']=preview
  small=Image.open(io.BytesIO(preview));small.thumbnail((128,128));buf=io.BytesIO();small.save(buf,format='PNG')
  entries['Metadata/plate_1_small.png']=buf.getvalue()
  with zipfile.ZipFile(f,'w',zipfile.ZIP_DEFLATED) as z:
   for n,data in entries.items():z.writestr(n,data)
 print(f.name,'sliced',flush=True)
