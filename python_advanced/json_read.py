f=open("data.json","r")
import json
data=json.load(f)
print(data)
f.close()