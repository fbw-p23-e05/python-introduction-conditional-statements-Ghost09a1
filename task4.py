import math

# input
radius = float(input("Input the radius of the circle: "))

# pi*radius²
area = math.pi * radius ** 2
rounded_area = round(area, 2)

# Print 
print(f"The area of the circle with radius {radius} is: {rounded_area}")