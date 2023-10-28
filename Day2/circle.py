# Calculate the area and circumference of a circle given its radius􏰌
# real number. The program should allow for both integer and decimal values as input.

radius = float(input("Enter Radius of Circle : "))
area = (22/7)*radius**2  #formula for area of circle
circumference = 2 * (22/7) * radius

print ("Area of the circle is ", round(area,3))   #round off the answer to three decimal places.
print ("Circumference of the circle is", round(circumference,3) )