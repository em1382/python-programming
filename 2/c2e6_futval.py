# Programmer: Ellis Madagan
# File name: c2e6_futval.py
# Updated: 3/1/2016, added formatting.
# This program computes the value of an investment carried 10 years into the future

def main():
    print("This program calculates the future value of a multi-year investment.")
    initial = eval(input("Enter the amount to invest each year: "))
    apr = eval(input("Enter the interest rate: "))
    yrs = eval(input("Enter the number of years: "))

    p = initial
    
    for i in range(yrs):
        p = p * (apr + 1) + initial

    print("The value after", yrs, "years is: {0}.".format(p - initial))

if __name__ == "__main__":
    main()

