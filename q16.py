a = input("enter a sentence")
b = a.split()
for word in set(b):
    c = b.count(word)
    print(word,'occurs',c,'times')
        
