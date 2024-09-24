#! /bin/python3

x = int(input("Enter a number less than 25:\n"))
if x < 25:
    while x <= 25: 
        print(f"Inside the loop, my variable is {x}")
        x += 1
else:
    print(f"The number you entered ({x}) is not less than 25")
