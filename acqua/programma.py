# dal modulo importo solo le funzioni che mi interessano, nascondendo il resto
from calcolatore_tariffe import calcola_aziende, calcola_privati

def istogramma(li):
    for el in li:
        for i in range(el):
            print('*', end='') # stampa asterisco el volte senza andare a capo
        print() # a capo

tipologia = input("privato o azienda? (p/a)")


mesi = list(range(1,2+1))
consumi = []
tariffe = []
totale_annuo = 0

for m in mesi:
    consumo = int(input(f"inserisci consumo del mese {m}: "))
    tariffa = 0

    if tipologia == 'p':
        tariffa = calcola_privati(consumo)
    else:
        tariffa = calcola_aziende(consumo)

    totale_annuo += tariffa
    tariffe.append(tariffa)
    consumi.append(consumo)

istogramma(consumi)

print("tariffe per mese: ", tariffe)
print("consumi per mese: ", consumi)

for m in mesi:
    print(f'nel mese {m} hai consumato {consumi[m-1]} e speso {tariffe[m-1]:.2f} €')
    #print("{0:.2f} €".format(tariffe[m-1]))
