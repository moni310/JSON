dic={
    "shopping":
        { 
            "chaco":15,
            "Biscuits":50,
            "Diary_milk":30,
            "ice_cream":20,
        } 
}
user=input("do you want to buy or add---")
if user =="buy":
    user1=input("what do u want to buy---")
    quantity=int(input("how much do u want to buy pls tell quantity---"))
    if user1=="chaco":
        dic["shopping"]["chaco"]=dic["shopping"]["chaco"]-quantity
        print(dic)
    elif user1=="Biscuits":
        dic["shopping"]["Biscuits"]=dic["shopping"]["Biscuits"]-quantity
        print(dic)
    elif user1=="Diary_milk":
        dic["shopping"]["Diary_milk"]=dic["shopping"]["Diary_milk"]-quantity
        print(dic)
    elif user1=="ice_cream":
        dic["shopping"]["Diary_milk"]=dic["shopping"]["Diary_milk"]-quantity
        print(dic)
    else:
        print("sorry this is not avilable in this shop--")
elif user=="add":
    add=input("what do you want to add--")
    quan=int(input("enter in how much quantity ---"))
    dic["shopping"][add]=quan
    print(dic)
else:
    pass
