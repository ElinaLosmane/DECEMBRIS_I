ievaditais_skaitlis = int(input("Ievadiet skaitli:"))

# Piešķir vērtību faktoriālam
faktorials = 1

# Aprēķinu faktoriālu, izmantojot for ciklu
for skaitlis in range(1, ievaditais_skaitlis + 1):
    faktorials*= skaitlis

# Izvada rezultātu
print(f"Faktoriāls no {ievaditais_skaitlis} ir:{faktorials}")