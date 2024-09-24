#! /bin/python3
try:
	x = int(input())
	if x == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
except ValueError :
	print("not a number")