ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

#Pārbauda, vai ievadītais skaitlis dalās ar 3 un 7, izmantojot if priekšrakstu
if ievaditais_skaitlis % 3 == 0 and ievaditais_skaitlis % 7 == 0:
    print(f"{ievaditais_skaitlis} dalās gan ar 3, gan 7")
else:
    print(f"{ievaditais_skaitlis} nedalās gan ar 3, gan 7")