#!/bin/python3

def array_of_names(persons):
    return [f"{x.capitalize()} {y.capitalize()}" for x, y in persons.items()]
persons = {"jean": "valjean","grace": "hopper","xavier": "niel","fifi": "brindacier"}
print(array_of_names(persons))
