chiavi = ['nome', 'cognome']
diz = {}.fromkeys(chiavi, 0)
print(diz)

albergo1 = {
    'codice': 1,
    'denominazione': 'Hotel Byron',
    'stelle': 4,
    'indirizzo': 'via b, Rimini',
    'telefono': '123456486',
}

# accesso per chiave
print(albergo1.get('telefono'))
print(albergo1['telefono'])

telefono = albergo1.get('telefono', '000000')
print(telefono)

print("\nliste parallele chiavi-valore")
print(list(albergo1.keys()))
print(list(albergo1.values()))

print('\nlista di coppie')
print(list(albergo1.items()))
