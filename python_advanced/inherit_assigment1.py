class Company:
    def __init__(self):
        self.cname=input("Enter the company name:")
        self.location=input("Enter your company location:")

    def display_location(self):
        print("The company location is at ",self.location)


class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter employee ID:"))
        self.name=input("Enter your name:")
        self.designation=input("Enter your designation:")
        self.salary=int(input("Enter your salary:"))

    def display_details(self):
        print(self.cname)
        print(super().display_location())
        print(self.empid)
        print(self.name)
        print(self.designation)
        print(self.salary)

    def update_salary(self):
        self.salary=self.salary+(0.1*self.salary)
        print("new salary:",self.salary)


c=Employee()
c.display_details()
c.update_salary()
