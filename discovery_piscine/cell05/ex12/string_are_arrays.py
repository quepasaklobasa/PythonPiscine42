#!/bin/python3

import sys
import re
if len(sys.argv)-1 != 1:
    print ("none")
else:
    x = sys.argv[1]
    match = re.findall(r'z', x)
    if match == []:
        print("none")
    else:
        print('z' * len(match))
