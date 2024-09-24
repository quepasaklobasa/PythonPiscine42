#!/bin/python3

import sys
if len(sys.argv)-1 < 2:
    print("none")
else:
    i = len(sys.argv) - 1
    while i > 0:
        print (f"{sys.argv[i]}")
        i -= 1
