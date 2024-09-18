lista = [12,3,4,[5,6,[7,9]],11]

def splaszcz(lista):
    for el in lista:
        if type(el) == list:
            splaszcz(el)
         