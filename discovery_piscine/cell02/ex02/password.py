#! /bin/python3

import getpass

password = "Python is awesome"
p = getpass.getpass()
if p == password:
    print("ACCESS GRANTED :D")
else:
    print("ACCESS DENIED! D:")
