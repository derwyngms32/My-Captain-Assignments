import math

def area_of_circle(Radius):
    area = Radius**2*math.pi
    return area

Radius = float(input("Please Enter the Radius of the Circle:   "))
print("The Area of the circle with Radius ",Radius," is ",area_of_circle(Radius))
