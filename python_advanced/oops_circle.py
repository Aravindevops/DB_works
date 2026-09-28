class Circle:
    def __init__(self):
        self.radius=int(input("enter the radius of the circle:"))

    def getarea(self):
        print("area:",3.14*self.radius*self.radius)

    def getperimeter(self):
        print("perimeter:",3.14*2*self.radius)

c=Circle()

c.getarea()
c.getperimeter()