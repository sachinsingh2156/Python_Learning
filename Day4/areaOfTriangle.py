# Calculate the area of a triangle given its base and height using a function"
def areaOfTriangle(base, height):
    area = (1/2) * base * height
    return round(area, 2)


base = float(input("Enter the base of Triangle : "))
height = float(input("Enter the height of Triangle : "))

area = areaOfTriangle(base, height)

print("Area of the triangle = ", area)
