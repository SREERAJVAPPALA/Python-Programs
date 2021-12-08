list1=input("enter the first list of numbers:")
list1=list1.split()
list2=input("enter the second list of numbers:")
list2=list2.split()
list1=list(map(int,list1))
list2=list(map(int,list2))
if len(list1) == len(list2):
	print("both strings have same length ")
if sum(list1) == sum(list2):
	print("both lists have same sum ")
if set(list1) == set(list2):
	print("both list have same values ")
else:
	print("both lists are not same same ") 
	
