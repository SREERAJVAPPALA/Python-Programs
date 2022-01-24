
def factorial(num):
    if num == 1 or num == 0:
            return 1
    f = num * factorial(num-1)
    return f
    
    
num = int(input("enter the number : ")) 
fact = factorial(num)
print("the factorial of ",num,"is",fact)