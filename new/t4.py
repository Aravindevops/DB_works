#wap to create a list of 5 random 3 digit number
import random
l=[]
for i in range(5):
    l.append(random.randint(100,999))
print(l)
