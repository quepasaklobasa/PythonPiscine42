#!/bin/python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("That's not a name bruh")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
