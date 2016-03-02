# Programmer: Ellis Madagan
# File name: c2e10_convert.py
# Date: 9/4/2015
# Updated: 3/1/2016, updated main() call.

# This program converts pounds into tons.

def main():
    print("This program converts pounds into tons.")
    p = eval(input("Enter a value in pounds: "))
    t = p/2000
    print(p, "pounds is equal to", t, "tons.")

if __name__ == "__main__":
    main()
    
    
