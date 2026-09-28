class Parent:
    def m1(self):
        print("parent method1")

    def m2(self):
        print("parent method2")

p=Parent()
p.m1()

#inheritance

class Child(Parent):
    def m1(self):#overriding the parent class method1
        super().m1()#extending the parent class method1
        print("child overriding method1")


c=Child()

c.m1()
c.m2()