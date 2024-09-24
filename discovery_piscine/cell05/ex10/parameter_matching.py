#!/bin/python3

import sys
import re
if (len(sys.argv)-1 != 1):
        print("none")
else:
    x = re.escape(sys.argv[1])
    y = input("What was the parameter? ")
    if y == x:
        print("Ding ding ding! Awesome job! :)")
    else:
        print("Tough luck, babes. Better luck next time.")
