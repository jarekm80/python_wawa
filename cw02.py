punkt = (1, 81)

x,y = punkt

if 0<x<10 and 0<y<10:
    print("Lewy dolny róg") 
elif 10<x<90 and 0<y<100:
    print("Lewa krawędź") 
if 0<x<10 and 90<y<100:
    print("Lewy górny róg") 
elif 0<x<100 and 10<y<90:
    print("Górna krawędź") 

print (x,y)