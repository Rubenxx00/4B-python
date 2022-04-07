def istogramma(li):
    for el in li:
        for i in range(el):
            print('*', end='') # stampa asterisco el volte senza andare a capo
        print() # a capo

def istogramma2(li):
    for el in li:
        print('*' * el)

def estrai_lunghezza(parole, n):
    li = []
    for p in parole:
        if len(p) <= n:
            li.append(p)
    return li

def estrai_maggiorenni(nomi, età):
    # se hanno lunghezze diverse?
    if len(nomi) != len(età):
        return None

    magg = []
    for i in range(len(età)):
        if età[i] >= 18:
            magg.append(nomi[i])

    return magg

def acronimo(parole):
    acr = ''
    for p in parole:
        acr += p[0]
    return acr.upper()

def acronimo2(parole):
    s = ''
    for p in parole:
        iniziale = p[0]
        s += iniziale
    return s.upper()

def acronimo3(parole):
    s = ''
    for p in parole:
        s += p[0].upper()
    return s

print("\tESERCIZIO estrai lunghezza")
lista_parole = ["cane", "cammello", "contemporaneamente"]
nmax = 4
res = estrai_lunghezza(lista_parole, nmax)
print(res)

print("\n\tESERCIZIO istogramma")
istogramma([3,7,9,5])

print("\n\tESERCIZIO maggiorenni")
print("test 1")
nomi = ["maria", "greta", "giuseppe"]
età = [16, 19, 21]
print(estrai_maggiorenni(nomi, età))

print("test 2")
nomi = ["maria", "greta"]
età = [16, 19, 21]
print(estrai_maggiorenni(nomi, età))

print("\n\tESERCIZIO acronimo")
res = acronimo2(['sistemi', 'informativi', 'aziendali'])
print(res)
print(acronimo3(['Agenzia', 'Dogane', 'Monopoli']))



