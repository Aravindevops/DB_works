s="Hello World "
c=1
for i in range(len(s)):
    print("iteration:",i)
    if s[-i-1]!=" ": 
        if s[-i-1]==" ":
            c+=1
            print("count:",c)
print(i)
print(c)

