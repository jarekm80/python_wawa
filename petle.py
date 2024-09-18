liczby=[]
while True:
    wejscie = input("wprawadz liczbe, lub q: ")
    if wejscie == "q":
        break
    liczby.append(int(wejscie))

print(liczby)
print("liczb było: ",len(liczby))
print("z czego unikalnych: ",len(set(liczby)))
print("średnia wynosi: ",sum(liczby)/len(liczby))