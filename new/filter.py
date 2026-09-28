l=[1,2,3,4,5,6,7,8,9,10]
fruits=["apple","banana","mango","grapes","orange"]
print(list(filter(lambda x:x%2==0,l)))
print(list(filter(lambda x:x>3,l)))
print(list(filter(lambda x:x%2==0 and x>3,l)))
print(list(filter(lambda x:len(x)>5,fruits)))