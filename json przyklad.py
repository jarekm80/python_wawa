"""
napisz kod, ktory bedzie dzialal nastepujaco:

$ python baza.py
Odczyt czy zapis [o, z]: o
a: 10, b: 20
a: 11, b: 11

$ python baza.py
Odczyt czy zapis [o, z]: z
podaj a: 11
podaj b: 13

$ python baza.py
Odczyt czy zapis [o, z]: o
a: 10, b: 20
a: 11, b: 11
a: 11, b: 13

"""
import json
if input("Odczyt czy zapis [o, z]:") == "z":
    a = input("Podaj a\n")
    b = input("Podaj b\n")
    with open("danejson.json", "w") as f:
    json.dump((a,b), f)