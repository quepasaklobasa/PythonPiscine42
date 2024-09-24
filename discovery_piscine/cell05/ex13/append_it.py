#!/bin/python3

import sys
if len(sys.argv) - 1 < 1:
    print("none")
else:
    x = sys.argv
    x.pop(0)
    for arg in x:
        match arg:
            case _ if arg.endswith('ism'):
                continue
            case _:
                print(arg+'ism')

