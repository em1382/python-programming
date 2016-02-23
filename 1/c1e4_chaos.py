# Programmer: Ellis Madagan
# File name: c1e4_chaos.py
# Date: 9/3/2015

# A simple program illustrating chaotic behavior
def main():
    print("This program illustrates chaotic behavior")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)
main()
