#! /bin/python3

x = int(input("Enter the first number: "))
print(x)
y = int(input("Enter the second number: "))
print(y)
z = x * y
print(f"{x} x {y} = {z}")
if z > 0:
    print("The result is positive.")
elif z < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
