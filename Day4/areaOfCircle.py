# Write a function to calculate the area of a circle  given its radius.

def AreaOfCircle(radius):
    area = (22/7)*radius**2
    print("Area of circle = ", round(area, 2))


def circumferenceOfCircle(radius):
    circumference = 2*(22/7)*radius
    print("Circumference of Circle = ", round(circumference, 2))


r = float(input("Enter the radius : "))
AreaOfCircle(r)
circumferenceOfCircle(r)
