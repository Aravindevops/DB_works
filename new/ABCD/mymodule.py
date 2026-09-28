from Calculator import operations
from shapes import rectangle
from shapes import circle as c

print(operations.add(10,5))
print(operations.sub(10,5))
print(operations.mul(10,5))
print(operations.div(10,5))
print(rectangle.area_rectangle(10,5))
print(rectangle.perimeter_rectangle(10,5))
print(c.area_circle(10))
print(c.perimeter_circle(10))