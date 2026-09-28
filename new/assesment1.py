import functools

#1 Capitalize all names in a list
names1 = ['alin', 'arun', 'anu']
print(list(map(lambda x:x.capitalize(),names1)))
#2 Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
print(list(map(lambda x:x+"@gmail.com",users)))
#3 Filter out all empty strings from a list
words1 = ['hello', ' ', 'world', ' ', 'python']
print(list(filter(lambda x:x.strip(),words1)))
#4 Filter names that start with the letter 'A'
names2 = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(list(filter(lambda x:x.startswith('A'),names2)))
#5 Concatenate all strings in a list
words2 = ['Python', 'is', 'fun']
print(functools.reduce(lambda x,y:x+y,words2))
#6 Multiply all numbers in a list
nums1 = [2, 3, 4]
print(functools.reduce(lambda x,y:x*y,nums1,1))
#7 Extract First Character of Each Word
words3 = ["apple", "banana", "cherry"]
print(list(map(lambda x:x[0],words3)))
#8 Add 10 to Each Number
nums2 = [5, 10, 15]
print(list(map(lambda x:x+10,nums2)))



#9 Sum of positive even numbers
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
print(functools.reduce(lambda x,y:x+y,filter(lambda x:x>0 and x%2==0,l)))
#10 Sum of Positive Odd numbers
print(functools.reduce(lambda x,y:x+y,filter(lambda x:x>0 and x%2==1,l)))
#11 Sum of Negative  odd numbers
print(functools.reduce(lambda x,y:x+y,filter(lambda x:x<0 and x%2==1,l)))
#12 Sum of Negatve Even numbers
print(functools.reduce(lambda x,y:x+y,filter(lambda x:x<0 and x%2==0,l)))
#13 Count of Positive numbers
print(functools.reduce(lambda x,y:x+y,map(lambda x:1,filter(lambda x:x>0,l)),0))
#14 Count of Negative numbers
print(functools.reduce(lambda x,y:x+y,map(lambda x:1,filter(lambda x:x<0,l)),0))



#15 Convert all Strings to Integers [1,2,3,4]
nums3 = ["1", "2", "3", "4"]
print(list(map(lambda x:int(x),nums3)))


#16 print list of product names in Uppercase
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

print(list(map(lambda x:x['name'].upper(),p)))
#17 print products with price greater than 10000
print(list(filter(lambda x:x["price"]>10000,p)))
#18 Find the total price of all products
print(functools.reduce(lambda x,y:x+y,map(lambda x:x["price"],p)))









