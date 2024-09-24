#!/bin/python3

import sys
if len(sys.argv)-1 < 1:
    print ("none")
else:
    print(f"Parameters: {len(sys.argv) - 1}")
    x = sys.argv
    x.pop(0)
    for z in x:
        print(f"{z} = {(len(z))}")
