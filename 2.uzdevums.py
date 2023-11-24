# Definē skaitli 
skaitlis = 1

# Meklē pirmo skaitli, kura kvadrāts nav lielāks par 1000, izmantojot while ciklu
while skaitlis**2 <= 1000:
    skaitlis += 1

# Izvada rezultātu
print(f"Pirmais skaitlis, kura kvadrāts nav lielāks par 1000, ir: {skaitlis}")