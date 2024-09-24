#!/bin/python3

import sys
if len(sys.argv) - 1 < 1:
    print("none")
else:
    def downcaseit(i):
        print(i.lower())
    x = sys.argv
    x.pop(0)
    for arg in x:
        downcaseit(arg)
