# Write a program that asks the user to enter the radius of a circle. The program should cal-
# culate and display the area and circumference of the circle using πr2 for the area and 2πr
# for the circumference.
# Hint: You can either use 3.14159 as the value of pi (π) or add the statement “import math”
# to the start of the program and then use “math.pi” wherever you need the value of pi in the program.

import math

PI = math.pi

radius = float(input("Enter the radius of a circle: "))

circleArea = PI * radius**2
circleCircumference = 2 * PI * radius

print(f"Area: {circleArea:.2f}")
print(f"Circumference: {circleCircumference:.2f}")
