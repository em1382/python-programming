# This program calculates the volume and surface area of a sphere.
# Author: Ellis Madagan (em1382)

import math

def main():
    radius = float(input("Enter the radius of a sphere: "))

    volume = round((4/3) * math.pi * radius ** 3, 2)
    area = round(4 * math.pi * radius ** 2, 2)

    print("The volume is: {0}, and the surface area is: {1}.".format(volume, area))

if __name__ == "__main__":
    main()
