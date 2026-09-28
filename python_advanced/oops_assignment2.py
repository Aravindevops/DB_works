class Student:
    def __init__(self):
        self.name=input("enter the name:")
        self.rollno=int(input("enter the roll number:"))
        self.mark=int(input("enter the mark:"))

    def updatemark(self):
        self.mark=int(input("enter the updated mark:"))
        print("new mark",self.mark)

    def display(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)
        print("Student mark:",self.mark)

    
l=[]
while True:
    print("1.Add student\n2.update mark\n3.display student details\n4.search student\n5.delete student\n6.exit")
    x=int(input("enter your choice: "))
    if x==1:
        a=Student()
        l.append(a)
        print(l)

    elif x==2:
        s=int(input("enter the rollno:"))
        for i in l:
            if i.rollno==s:
                i.updatemark()
                break
            else:
                print("student doesn't exist")

    elif x==3:
        s=int(input("enter the rollno:"))
        for i in l:
            if i.rollno==s:
                i.display()
                break
            else:
                print("student doesn't exist")

    elif x==4:
        s=int(input("enter the rollno:"))
        for i in l:
            if i.rollno==s:
                print("Student exists")
                break
            else:
                print("student doesn't exist")

    elif x==5:
        s=int(input("enter the rollno:"))
        for i in l:
            if i.rollno==s:
                l.remove(i)
                print("student removed")
                break
            else:
                print("student doesn't exist")

    elif x==6:
        print("Exit")
        break

