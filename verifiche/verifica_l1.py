def istogramma(li):
    for el in li:
        for i in range(el):
            print('*', end='') # stampa asterisco el volte senza andare a capo
        print() # a capo

def istogramma2(li):
    for el in li:
        print('*' * el)

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
        s += p[0]
    return s.upper()

def acronimo3(parole):
    s = ''
    for p in parole:
        s += p[0].upper()
    return s

print("\tESERCIZIO 1")
istogramma([3,7,9,5])

print("\n\tESERCIZIO 2")
print("test 1")
nomi = ["maria", "greta", "giuseppe"]
età = [16, 19, 21]
print(estrai_maggiorenni(nomi, età))

print("test 2")
nomi = ["maria", "greta"]
età = [16, 19, 21]
print(estrai_maggiorenni(nomi, età))

print("\n\tESERCIZIO 3")
print(acronimo2(['sistemi', 'informativi', 'aziendali']))
print(acronimo3(['Agenzia', 'Dogane', 'Monopoli']))



""" 
istogramma([7,0,6])
istogramma([10])
istogramma([])
istogramma([0]) """