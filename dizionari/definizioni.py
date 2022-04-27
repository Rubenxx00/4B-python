studente = {
    'nome': 'mario',
    'cognome': 'rossi',
    'anno_nascita': 2002,
    'classe': '4B SIA'
}

print(studente['nome'], studente['cognome'])
print(studente.get('classe'))

# dizionario che rappresenti un albergo
albergo1 = {
    'codice': 1,
    'denominazione': 'Hotel Byron',
    'stelle': 4,
    'indirizzo': 'via b, Rimini',
    'telefono': '123456486',
}

albergo2 = {
    'codice': 2,
    'denominazione': 'Hotel Polazzi',
    'stelle': 3,
    'indirizzo': 'via p, Milano Marittima',
    'telefono': '194556486',
}

print(albergo1)

# stampare il nome dell'albergo con più stelle fra i due
if albergo1['stelle'] > albergo2['stelle']:
    print(albergo1['denominazione'])
else:
    print(albergo2['denominazione'])
