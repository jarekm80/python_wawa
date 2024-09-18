import sys
try:

plik="cw01.py"
with open(plik) as f:
    for nr,line in enumerate(f):
        print(f"{nr:4} {line}")