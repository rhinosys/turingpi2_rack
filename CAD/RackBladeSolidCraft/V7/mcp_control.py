"""Session MCP locale autorisée ; sauvegarde chaque réponse pour l'audit V7."""
import subprocess,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=subprocess.Popen(['/Applications/SolidCraft.app/Contents/MacOS/solidcraft-cli','mcp','--headless','--allow-path',str(ROOT.parent)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
serial=0
def rpc(method,params):
 global serial
 serial+=1
 p.stdin.write(json.dumps({'jsonrpc':'2.0','id':serial,'method':method,'params':params})+'\n');p.stdin.flush()
 while True:
  line=p.stdout.readline()
  if not line:raise RuntimeError('MCP fermé')
  result=json.loads(line)
  if result.get('id')==serial:return result
rpc('initialize',{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'rack-v7','version':'1'}})
p.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n');p.stdin.flush()
print('MCP prêt',flush=True)
for line in sys.stdin:
 try:
  q=json.loads(line);label=q.pop('_label',str(serial+1))
  if '_file' in q:q=json.loads((ROOT/q['_file']).read_text())
  result=rpc('tools/call',q)
  (ROOT/'verification'/f'{label}.json').write_text(json.dumps(result,indent=2))
  texts=[x['text'] for x in result.get('result',{}).get('content',[]) if x.get('type')=='text']
  print(label,('\n'.join(texts))[:700],flush=True)
 except Exception as e:print('ERROR',repr(e),flush=True)
p.terminate()
