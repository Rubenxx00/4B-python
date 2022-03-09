n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))

if n1 > n2:
    print(n2, n1, sep="->")
else:
    print(f"{n1} -> {n2}")