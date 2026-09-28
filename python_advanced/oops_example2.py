class Student:
    def __init__(self):
        print("Enter the details of the student")
        self.rollno=int(input("Enter rollno: "))
        self.name=input("Enter name: ")
        self.mark1=int(input("Mark 1: "))
        self.mark2=int(input("mark2: "))
        self.mark3=int(input("mark3: "))


    def display(self):

        print("Roll No:",self.rollno)
        print("Total Mark: ",self.mark1+self.mark2+self.mark3)

s1=Student()
s2=Student()

s1.display()
s2.display()
