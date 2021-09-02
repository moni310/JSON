import json
data={"name":"moni","age":20}
file =open("myfile.json","w")
json.dump(data,file,indent=4)
print(file)
file.close()