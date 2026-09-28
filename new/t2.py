#write a to find the count of a specific character in a string

s="hello world"
ch="l" 
count=0

for i in s:
    if i==ch:
        count+=1

print("count : ",count)