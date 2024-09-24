#! /bin/python3

try:
    x = float(input("Give me a number: "))
    if x.is_integer():
        print("Your number is a integer")
    else:
        print("Your number is a float")

except ValueError:
    print("Let's stick to numbers, sweetheart")
