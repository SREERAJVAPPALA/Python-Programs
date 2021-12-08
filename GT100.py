string=input("enter the integers")
list_=string.split()
list2_=[]

for i in list_:
	if int(i)>100:
		list2_.append("over")
	else:
		list2_.append(int(i))
print(list2_)
