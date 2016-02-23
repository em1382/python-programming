# Programmer: Ellis Madagan
# File name: c1e3_chaos.py
# Date: 9/3/2015

# A simple program illustrating chaotic behavior
# This version differs in that the output eventually levels out to 0.5
def main():
    print("This program illustrates chaotic behavior")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
main()
