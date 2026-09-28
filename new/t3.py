#write a program to create new dictionary where keys are letters and values are their counts in a given string
"""
s="hello world"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""

s="hello world"
d={}
for i in s:
    if (i.isalpha()):
        d[i]=s.count(i)
print(d)