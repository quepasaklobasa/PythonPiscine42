#!/bin/python3

import sys
import re
if (len(sys.argv)-1 != 2) or not sys.argv[1] or not sys.argv[2]:
        print("none")
else:
    try:
        x = len(re.findall(re.escape(sys.argv[1]), sys.argv[2]))
        print(x)
    except SyntaxError:
        print ("Stop it, cheeky bastard!")
