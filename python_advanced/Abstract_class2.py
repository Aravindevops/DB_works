from abc import ABC,abstractmethod

class Employee(ABC):
    
    def __init__(self):
        self.name=input("Enter the name of the employee:")
        self.empid=int(input("Enter the employee id:"))
        self.age=int(input("Enter the age of the employee:"))
    @abstractmethod
    def calcualte_salary(self):
        pass


class Fulltime(Employee):

    
    def __init__(self):
        Employee.__init__(self)
        self.salary=int(input("Enter the salary:"))

    def calcualte_salary(self):
        print("Full time employee salary:",self.salary)

class Parttime(Employee):


    def __init__(self):
        Employee.__init__(self)
        self.hourly_rate=int(input("Enter the hourly rate:"))
        self.hours_worked=int(input("Enter the hours worked:"))

    def calcualte_salary(self):
        print("Part time employee salary:",self.hourly_rate*self.hours_worked)

f=Fulltime()
f.calcualte_salary()

p=Parttime()
p.calcualte_salary()