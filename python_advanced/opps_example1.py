class Employee:
    def __init__(self,empid,name,age,place,salary,designation):
        self.empid=empid
        self.name=name
        self.age=age
        self.place=place
        self.salary=salary
        self.designation=designation

    def getsalary(self):
        print("Salary:",self.salary)

    def showpersonaldetails(self):
        print("Employee id:",self.empid)
        print("Employee name:",self.name)
        print("Age:",self.age)
        print("Place:",self.place)
        print("Designation:",self.designation)


name=input("Enter name: ")
age=int(input("Enter age: "))
empid=int(input("Enter employee id: "))
place=input("Enter place: ")
salary=int(input("Enter salary: "))
designation=input("Enter designation: ")

Employee=Employee(empid,name,age,place,salary,designation)
Employee.showpersonaldetails()
Employee.getsalary()