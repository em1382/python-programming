# Programmer: Ellis Madagan
# File name: c2e7_futval.py
# Date: 9/5/2015

# This program calculates a compound interest rate

def main():
    print("This program calculates a compound interest rate over 10 years.\n")
    prin = eval(input("Enter the initial amount: "))
    rate = eval(input("Enter the yearly rate: "))
    period = eval(input("Enter the number of compounding periods: "))
    
    # This is a way of doing it without a loop...
    # b = 1 + (rate/period)
    # ex = comp/10
    # total = init * pow(b, ex)
    # print(total)

    for i in range(10 * period):
        prin += rate/period / 10

    print("The total is:", prin)
main()
