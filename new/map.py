l=[1,2,3,4]
k=['red','green','blue','yellow','black']
d=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},{'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},{'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
print(list(map(lambda x:x**2,l)))
print(list(map(lambda x:x**3,l)))
print(list(map(lambda x:x**0.5,l)))
print(list(map(lambda x:len(x),k)))
print(list(map(lambda x:x[0],k)))
print(list(map(lambda x:x[-1],k)))
print(list(map(lambda x:x[::-1],k))) #reverse of string
print(list(map(lambda x:x+10,l)))
print(list(map(lambda x:x["email"],d)))

