import json
emp1=["neelam","programer","24","2400",]
emp2=["komal","trainer","24","20000"]
emp3=["anuradha","HR","25","40000"]
emp4=["Abhishek","manager","29","63000"]
emp=["name","Destigation","age","Salery"]
a=zip(emp,emp1)
b=zip(emp,emp2)
c=zip(emp,emp3)
d=zip(emp,emp4)
list1=["emp1","emp2","emp3","emp4"]
list2=[dict(a),dict(b),dict(c), dict(d)]
dict1=zip(list1,list2)
print(dict(dict1))
ques8=json.dumps(dict(dict1))
file=open("ques8.json","w+")
json.dump(ques8,file,indent=4)
file.close
print(ques8)
user=input("which employee data do u want to see emp1 / emp2/ emp3/emp4--\n")
if user=="emp1":
    print(list2[0])
elif user=="emp2":
    print(list2[1])
elif user=="emp3":
    print(list2[2])
elif user=="emp4":
    print(list2[3])
else:
    pass


