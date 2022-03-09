from math import sqrt

# funzione
def aggiungi(x, y):                                    
    print("x è {} e y è {}".format(x, y))
    return x + y

def sottrai(x, y):                                    
    print("x è {} e y è {}".format(x, y))
    return x - y

def distanza(x1, y1, x2, y2):
    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

# procedura
def stampa_lista_reverse(li):
    for i in li[::-1]:
        print(i, end=" ")

# posso richiamare le funzioni quante volte voglio
risultato = aggiungi(1, 5)
risultato2 = aggiungi(2, 5)
risultato3 = aggiungi(3, 5)

print(risultato)

# esempio di calcolo distanza

x1 = int(input("inserisci la x del primo"))
y1 = int(input("inserisci la y del secondo"))
x2 = int(input("inserisci la x del primo"))
y2 = int(input("inserisci la y del secondo"))

d = distanza(x1, y1, x2, y2)

print("la distanza è ", d)
