# What area calculate? [CIRCLE OR RECTANGLE]
# I: rectangle
# O: give me height
# I: 10
# O: give me width
# I: 5
# O: The result is 50

# What area calculate? [CIRCLE OR RECTANGLE]
# I: CIRCLE
# O: give me radius
# I: 10
# O: The result is 314.0
import math

def circleArea():
    radius = float(input("Give me radius:"))
    return round(radius * radius * math.pi, 1)

def rectangleArea():
    height = float(input("Give me height:"))
    width = float(input("Give me width:"))
    return height * width

commando = input("What area calculate? [CIRCLE OR RECTANGLE]")

if commando == "circle":
    result = circleArea()
    print(result)
else:
    result = rectangleArea()
    print(result)