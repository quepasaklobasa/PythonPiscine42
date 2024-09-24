#!/bin/python3

import math
try:
    x = float(input("Give me a number: "))
    z = math.ceil(x)
    print(z)
except ValueError:
    print("I said numbers, mfkr")
