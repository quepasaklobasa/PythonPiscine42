#!/bin/python3

x = [2, 8, 9, 48, 8, 22, -12, 2]
y = [z + 2 for z in x if z > 5]
print(f"Original array: {x}")
print(f"New array: {y}")

