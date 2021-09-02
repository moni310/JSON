import json
object={"a":"banglore","b":"up"}
file=open("object.json","w")
json.dump(object,file,indent=4)
print(type(file))
file.close
