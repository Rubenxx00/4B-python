li = ["a", "b", "c", "d", "e"]

for i in li:
    if i == "c":
        break
    print(i.upper(), end=" ")

print("il programma continua")

# stampo tutte le lettere della lista trasformate in maiuscolo TRANNE la "c"

li = ["a", "b", "c", "d", "e"]

for i in li:
    if i == "c":
        continue # il corpo del for viene saltato (salta l'iterazione corrente)
    print(i.upper(), end=" ")

print("fine")
