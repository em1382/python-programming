# Programmer: Ellis Madagan
# File name: c1e6c_chaos.py
# Date: 9/3/2015

# A simple program illustrating chaotic behavior
def main():
    print("This program illustrates chaotic behavior")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100): # Prints 100 lines instead of 10.
        x = 3.9 * x - 3.9 * x * x
        print(x)
main()

# The output of the three different versions of starts out similar,
# but begins to differ greatly near the end. I'm not sure why this is.
