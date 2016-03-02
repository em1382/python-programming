# Name: Ellis Madagan
# File name: c2e1_convert.py
# Date: 9/3/2015
# Updated 3/1/2016, added formatting.

# This program prints a self-description

def main():
    print("This program converts Celsius to Fahrenheit.")
    c = eval(input("What is the temperature in Celsius?: "))
    f = (9/5 * c + 32)
    print("The temperature in Fahrenheit is {:0.2f}\u00b0.".format(f))
main()
