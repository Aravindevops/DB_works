from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class rectangle(shape):
    def __init__(self):
        self.length=int(input("enter the length of the rectangle:"))
        self.breadth=int(input("enter the breadth of the rectangle:"))

    def area(self):
        print("area:",self.length*self.breadth)

    def perimeter(self):
        print("perimeter:",2*(self.length+self.breadth))


class square(shape):
    def __init__(self):
        self.side=int(input("enter the side of the square:"))

    def area(self):
        print("area:",self.side*self.side)

    def perimeter(self):
        print("perimeter:",4*self.side)


r=rectangle()
r.area()
r.perimeter()

s=square()
s.area()
s.perimeter()