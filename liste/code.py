
coda_p1 = []
coda_p2 = []

def accoda(elemento, priorità):
    # salto controlli di validità (priorità fra 1 e 2)
    if priorità == 1:
        coda_p1.append(elemento)
    else:
        coda_p2.append(elemento)

def esegui():
    # fin quando ho elementi di priorità 1, estraggo da quella coda
    if len(coda_p1) != 0:
        return coda_p1.pop(0)
    elif len(coda_p2) != 0:
        # se ho finito gli elementi di priorità 1, estraggo dalla seconda coda
        return coda_p2.pop(0)
    else:
        # se entrambe le code sono vuote
        return None

def stampa_code():
    coda = coda_p1 + coda_p2
    for i in range(len(coda)):
        print(f'{i}: {coda[i]}')

accoda('A', 1)
accoda('B', 1)
accoda('X', 2)
accoda('Y', 2)
accoda('Z', 2)
accoda('a', 1)

stampa_code()

# li estraggo tutti
estratto = esegui()
while estratto != None:
    print(f"estraggo l'elemento {estratto}")
    estratto = esegui()
