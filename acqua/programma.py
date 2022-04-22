from calcolatore_tariffe import calcola_aziende, calcola_privati

def istogramma(li):
    for el in li:
        for i in range(el):
            print('*', end='') # stampa asterisco el volte senza andare a capo
        print() # a capo

tipologia = input("privato o azienda? (p/a)")

# TODO: chiedere consumo per ogni mese e calcolare l'importo corrispondente. Salvare i risultati e disegnare l'istogramma dei consumi nell'arco dei 12 mesi

mesi = list(range(1,12+1))
consumi = []

for m in mesi:
    consumo = int(input(f"inserisci consumo del mese {m}: "))
    tariffa = 0

    if tipologia == 'p':
        tariffa = calcola_privati(consumo)
    else:
        tariffa = calcola_aziende(consumo)

    consumi.append(consumo)

istogramma(consumi)