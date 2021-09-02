
import json
data='{"name":"moni","age":20}'
data1=json.loads(data)
print(data1)
print(data1["age"])