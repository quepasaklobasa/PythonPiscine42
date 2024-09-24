#!/bin/python3

def find_the_redheads(dupont_family): return list(filter(lambda key: dupont_family[key] == "red", dupont_family.keys()))
dupont_family = {
        "florian":"red",
        "marie":"blond",
        "virginie":"brunette",
        "david":"red",
        "franck":"red"
        }

print(find_the_redheads(dupont_family))
