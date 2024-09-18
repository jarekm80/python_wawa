import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/?format=json")

# print(response.status_code)
data = response.json()
kursy = data[0]["rates"]

for kurs in kursy:
    print(f"{kurs['code']}: {kurs['mid']}")


import tkinter as ttk

def jakas_funkcja():
    text = pole.get()
    # op = operacja.get()
    if op == "a":
        p_t = text.lower()
    else:
        p_t = text.upper()

    wynik.configure(text=p_t)

root = ttk.Tk()
root.title("GUI walutowe")

label_waluta = ttk.Label(root, text="Podaj walute")
label_waluta.pack()

waluta = ttk.Entry(root)
waluta.pack()

label_ilosc = ttk.Label(root, text="Podaj ilosc")
label_ilosc.pack()

ilosc = ttk.Entry(root)
ilosc.pack()

button = ttk.Button(root, text="wykonaj", command=jakas_funkcja)
button.pack()

wynik = ttk.Label(root, text="-")
wynik.pack()

root.mainloop()