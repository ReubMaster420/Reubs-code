import random
radius = random.randint(5,20)
print("Radius =",radius)
def circumference (radius):
    radius = 2*radius*3.14
    return radius
def area (radius):
    radius = radius*radius*3.14
    return radius
y = area(radius)
z = circumference(radius)
print("Area =",y,"and Circumference =",z)
