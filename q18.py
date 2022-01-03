a = int(input("enter the number"))
rev = 0
while(a>0):
	dig = a%10
	rev = rev*10 + dig
	a = a//10
print("reverse of the number:",rev)
