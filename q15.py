a=input("enter a string")
b=" "
b=b+a[0]
for i in range(1,len(a)):
	if a[i]==a[0]:
		b=b+'$'
	else :
		b=b+a[i]
print(b)
