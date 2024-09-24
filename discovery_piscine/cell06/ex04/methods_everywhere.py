#!/bin/python3

import sys
if len(sys.argv) - 1 < 1:
    print("none")
else:
    def shrink(i):
        a = slice(8)
        print(i[a])
    def enlarge(i):
        print(i + 'Z' * (8-len(i)))
    x = sys.argv
    x.pop(0)
    for arg in x:
        if len(arg) >= 8:
            shrink(arg)
        elif len(arg) == 8:
            print(arg)
        else:
            enlarge(arg)
