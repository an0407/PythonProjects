import math

a = 3.16
b = 9
c = 9.128
print(round(a))
print(math.sqrt(b))
print(math.ceil(c))
print(math.floor(c))
print(math.pi)

radius = float(input("Enter a radius: "))
print(f"The circumference is: {2*math.pi*radius}")
print(f"The area is: {math.pi*pow(radius, 2)}")

base = float(input("Enter a base of a right angle triangle: "))
height = float(input("Enter a height of a right angle triangle: "))
print(f"The Hypotenuese of the right angle triangle is {math.sqrt(pow(base,2)+pow(height,2))}")

