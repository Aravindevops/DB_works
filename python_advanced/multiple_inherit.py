class Hospital:
    def __init__(self):
        self.hos_nam=input("enter hospital name:")
        self.location=input("enter location name:")
        self.phone=int(input("enter phone number:"))

    def display_hospital(self):
        print(self.hos_nam)
        print(self.location)
        print(self.phone)

class Department:

    def __init__(self):
        self.dept_name=input("Enter dept name:")
        self.doctor_name=input("enter doctor's name:")


    def display_department(self):
        print(self.dept_name)
        print(self.doctor_name)


class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("enter patient name:")
        self.age=int(input("enter the patient age:"))
        self.gender=input("enter gender:")
        self.adm_date=input("enter admission date:")
        self.bedno=int(input("enter bed number:"))
        self.dis_date=input("enter discharge date:")


    def set_discharge(self):
        print(self.dis_date)

    def full_summary(self):
        self.display_hospital()
        self.display_department()
        print(self.patient_name)
        print(self.age)
        print(self.gender)
        print(self.adm_date)
        print(self.bedno)
        print(self.dis_date)


p=Patient()

p.full_summary()



    