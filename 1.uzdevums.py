ievaditais_skaitlis = int(input("Ievadiet skaitli:"))

# Piešķir vērtību summai
summa=0

# Saskaitu skaitļus, izmantojot for ciklu
for skaitlis in range (1,
ievaditais_skaitlis + 1):
    summa+=skaitlis

# Izvadu rezultātu
print(f"Summa no 1 līdz {ievaditais_skaitlis} ir: {summa}")

