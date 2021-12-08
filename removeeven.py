list_=input("enter the list of integers").split()
newlist=[]
for i in list_:
	if int(i) %2 != 0:
		newlist.append(int(i))

print("the new list without even numbers",newlist)


		

 
