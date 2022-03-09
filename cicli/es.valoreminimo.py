
# VERSIONE 1 (limitato)
# inserito in input n numeri, comunicare quello più piccolo
n=int(input('inserisci lunghezza: '))
min=10000000
for i in range (1, n+1):
    numero=float(input('inserisci valore: '))
    if numero<min:
        min=numero
print(f'il valore minimo è: {min}')

# VERSIONE 2
# inserito in input n numeri, comunicare quello più piccolo
n=int(input('inserisci lunghezza: '))
for i in range (1, n+1):
    numero=float(input(f'inserisci valore {i}:'))
    if i == 1:
        print("sono alla prima iterazione, inizializzo min")
        min = numero
    else:
        if numero<min:
            print("trovato un numero minore di min, quindi aggiorno min")
            min=numero

print(f'il valore minimo è: {min}')


