# This program calculates the cost per square inch of a pizza,
# given the diameter and price.
# Author: Ellis Madagan (em1382)

import math

diameter = float(input("Enter the diameter of the pizza: "))
price = float(input("Enter the cost of the pizza: "))

radius = diameter / 2
area = math.pi * radius ** 2

print("The cost of the pizza per square inch is: {0}.".format(round(price / area, 2)))
