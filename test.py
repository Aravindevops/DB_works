haystack="hello world"
needle="world"

length_hay=len(haystack)
length_needle=len(needle)
count=0

for i in range(0,length_needle):
    while count!=length_needle:
        for j in needle:
            if j==haystack[i]:
                count+=1
            else:
                count=0
print(i)

    

                
