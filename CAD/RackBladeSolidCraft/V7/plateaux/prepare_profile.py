from pathlib import Path
import json,zipfile
P=Path(__file__).resolve().parent
with zipfile.ZipFile(P.parents[1]/'Tolerances/Rack_Tolerance_PETG_Noir_X1C.3mf') as z:d=json.loads(z.read('Metadata/project_settings.config'))
R=Path('/Applications/BambuStudio.app/Contents/Resources/profiles/BBL/filament')
seen=set();keys=set()
def visit(name):
 if name in seen:return
 seen.add(name);f=R/(name+'.json')
 if not f.exists():raise FileNotFoundError(f)
 x=json.loads(f.read_text());keys.update(x)
 if x.get('inherits'):visit(x['inherits'])
 for n in x.get('include',[]):visit(n)
visit('Bambu PETG HF @BBL X1C')
keys.update(k for k in d if k.startswith('filament_'))
keys.update(['default_filament_colour','default_filament_profile','different_settings_to_system','extruder_ams_count'])
changes={}
for k in keys:
 if k in d and isinstance(d[k],list) and len(d[k]) in [2,4]:
  old=d[k];d[k]=old[len(old)//2:];changes[k]=[old,d[k]]
d.update(filament_colour=['#000000'],filament_multi_colour=['#000000'],filament_settings_id=['Bambu PETG HF @BBL X1C'],filament_ids=['GFG02'],default_filament_profile=['Bambu PETG HF @BBL X1C'],flush_volumes_matrix=['0'],flush_volumes_vector=['140','140'],enable_prime_tower='0',curr_bed_type='High Temp Plate',print_sequence='by layer')
(P/'profil_PETG_HF_noir_X1C.json').write_text(json.dumps(d,indent=2))
(P/'verification/profile-normalization.json').write_text(json.dumps(changes,indent=2))
print('Filament keys',len(keys),'changes',len(changes),'temperatures',d['nozzle_temperature'])
