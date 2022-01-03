str1=input("enter the first string")
str2=input("enter the second string")
x=str1[0]
str1=str1.replace(str1[0],str2[0])
str2=str2.replace(str2[0],x)
print(str1 ,str2)

