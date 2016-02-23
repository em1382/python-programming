# Programmer: Ellis Madagan
# File name: c1e7_chaos.py
# Date: 9/3/2015

# A simple program illustrating chaotic behavior
def main():
    print("This program illustrates chaotic behavior")
    x = eval(input("Enter a number between 0 and 1: "))
    x2 = eval(input("Enter another number between 0 and 1: "))
    print("{0:<20}".format("Value one:"), "{0:<20}".format("Value two:"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        x2 = 3.9 * x2 * (1 - x)
        print("{0:<20}".format(x), "{0:<20}".format(x2))
main() 
