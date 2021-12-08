def new_dict():
    limit=int(input("enter no of elements"))
    a={}
    for i in range(0,limit):

        key=  int(input("enter key"))
        value=input("enter value")
        a[key]= int(value)
    return a
print("enter the first dictionary")
dic1=new_dict()
print("enter the second dictionary")
dic2=new_dict()
print(dic1)
print(dic2)
dic3={}
for key in dic1:
	dic3[key]=dic1[key]
for key in dic2:
	if key in dic3:
		dic3[key]=dic3[key]+dic2[key]
	else:
		dic3[key]=dic2[key]
print(dic3)



