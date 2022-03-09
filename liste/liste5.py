# caricare da codice una lista di 5 elementi
# stampare quelli in posizione pari, preceduti da "posizione i: "

li = ["casa", "palestra", "ufficio", "ospedale"]

for i in range(4):
    if i%2 == 0:
        print(f"posizione {i}: {li[i]}")

# caricare una lista di N (chiesto in input) interi chiedendo in input ogni elemento
# stampare il doppio di ogni elemento

# Esempio
# I: 1, 2, 3, 4

# O: 2, 4, 6, 8

N = int(input("Quanti vuoi inserire?"))
li = []
for i in range(N):
    li[i] = int(input("Inserisci il numero"))
    