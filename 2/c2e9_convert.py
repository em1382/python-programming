# Name: Ellis Madagan
# File name: c2e9_convert.py
# Date: 9/4/2015
# Updated: 3/1/2016, updated main() call.

# This program converts distance in kilometers into miles

def main():
    print("This program converts kilometers into miles.")
    k = eval(input("Enter a distance in kilometers: "))
    m = k * 0.62
    print(k, "kilometers is", m, "miles.")

if __name__ == "__main__":
    main()
    
