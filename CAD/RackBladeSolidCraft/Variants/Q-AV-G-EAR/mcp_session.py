import subprocess,json,sys
p=subprocess.Popen(['/Applications/SolidCraft.app/Contents/MacOS/solidcraft-cli','mcp','--allow-path','./CAD/RackBladeSolidCraft'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
i=0
def rpc(method,params):
 global i
 i+=1;p.stdin.write(json.dumps({'jsonrpc':'2.0','id':i,'method':method,'params':params})+'\n');p.stdin.flush()
 while True:
  line=p.stdout.readline()
  if not line:raise RuntimeError('MCP fermé')
  r=json.loads(line)
  if r.get('id')==i:return r
print(json.dumps(rpc('initialize',{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'rack-variant','version':'1'}})),flush=True)
p.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n');p.stdin.flush()
print(json.dumps(rpc('tools/list',{})),flush=True)
for line in sys.stdin:
 try:
  r=json.loads(line);print(json.dumps(rpc('tools/call',r)),flush=True)
 except Exception as e:print(str(e),flush=True)
p.terminate()
