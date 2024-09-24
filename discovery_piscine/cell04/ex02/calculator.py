#! /bin/python3

try:
    x = int(input("Give me the first number: "))
    y = int(input("Give me the second number: "))
    print("Thank you!")
    a = x + y
    b = x - y
    c = x / y
    d = x * y
    print(f"{x} + {y} = {a}")
    print(f"{x} - {y} = {b}")
    print(f"{x} / {y} = {c}")
    print(f"{x} * {y} = {d}")
except ValueError:
    print("Let's stick to numbers, love")
except ZeroDivisionError:
    print("You can't divide by zero, thus, your second number was maliciously chosen")
