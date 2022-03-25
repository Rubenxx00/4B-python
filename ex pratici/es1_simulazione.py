def palindroma(s):
    return s == s[::-1]

def media(li):
    somma = 0
    for el in li:
        somma += el
    return somma / len(li)

def mediana(li):
    li = sorted(li)
    n = len(li)

    if len(li) % 2 != 0:
        pos_centrale = len(li) // 2
        return li[pos_centrale]
    else:
        pos_centrale1 = n // 2 - 1   # centrale di sinistra
        pos_centrale2 = n // 2  # centrale di destra 
        # uguale a scrivere:
        # pos_centrale2 = pos_centrale1 + 1  # centrale di destra (cioè il successivo)
        
        m = (li[pos_centrale1] + li[pos_centrale2]) / 2 # media dei 2 elementi centrali
        return m

def mediana2(li):
    return li[len(li)//2] if len(li) % 2 else (li[len(li)//2 - 1] + li[len(li)//2]) / 2



    "a" if a>b else "b"



def palindroma2(s):
    s_reverse = s[::-1]
    if s == s_reverse:
        return True
    else:
        return False

print("inizio programma")
stringa = input("inserisci la stringa da verificare: ")
if palindroma2(stringa) == True:
    print("è palindroma")
else:
    print("non è palindroma")

li = [] # lista vuota
el = int(input("inserisci il primo elemento (0 per terminare): "))
while el != 0: # riempio fino a quando utente non inserisce 0
    li.append(el)
    el = int(input("inserisci il primo elemento (0 per terminare): "))
# stampo media e mediana (invoco le funzioni definite prima)
print(media(li))
print(mediana(li))