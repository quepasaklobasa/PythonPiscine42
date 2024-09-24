#!/bin/python3

import sys
if len(sys.argv) - 1 != 2:
    print("none")
else:
    x = sys.argv
    a = int(x[1])
    b = int(x[2])
    if b > a:
        array = [y for y in range(a, b+1)]
        print(array)
    else:
        print("Not the assignment :D")
