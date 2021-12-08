clrlist_one=input("enter the colours in list1:").split()
clrlist_two=input("enter the colours in list2:").split()
print("list 1=",clrlist_one)
print("list 2=",clrlist_two)
l=[]
for i in range(0,len(clrlist_one)):
	if clrlist_one[i] not in clrlist_two:
		l.append(clrlist_one[i])
print(l)

