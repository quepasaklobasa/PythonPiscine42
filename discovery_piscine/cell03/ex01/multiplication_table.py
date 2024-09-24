#! /bin/python3

x = int(input("Enter a number: \n"))
y = 0
while y < 10:
    z = x * y
    print(f"{y} x {x} = {z}")
    y += 1
