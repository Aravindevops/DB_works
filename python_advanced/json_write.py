f=open("data.json","w")
import json
data=[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
json.dump(data,f)
f.close()