#Circle Calculator
import math

radius = float(input("Radius: "))
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius

print(f"The Area is {round(area, 2)}cm")
print(f"The Circumference is {round(circumference, 2)}cm")