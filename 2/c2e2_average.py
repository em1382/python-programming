# Programmer: Ellis Madagan
# File name: c2e2_average.py
# Date: 9/4/2015 (I date all of these as a personal aid, I know it's not required)
# Updated 3/1/2015, added formatting.

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three exam scores seperated by a comma: "))
    avg = (score1 + score2 + score3) / 3
    print("The average is {0}.".format(avg))
main()
