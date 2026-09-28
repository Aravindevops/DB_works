class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

    def show(self):
        print(self.name,self.age)


name=input("enter name: ")
age=int(input("enter age: "))
person1=Person(name,age)
person2=Person("Bob",25)
person1.show()