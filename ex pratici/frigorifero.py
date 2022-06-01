# gestionale delle scadenze dei prodotti nel frigorifero
# inseriamo n prodotti con relativa data di scadenza
# stampiamo quei prodotti con scadenza inferiore a una settimana, ordinati dal più prossimo in giù
from datetime import date, datetime

# parsing da stringa a data
def leggi_data(stringa) -> date:
    date_time_obj = datetime.strptime(stringa, "%d/%m/%y") #1/6/22
    return date_time_obj.date()

frigorifero = []

for i in range(3):
    nome_prod = input("inserisci il nome del prodotto: ")
    data_str = input("inserisci la data di scadenza: ")
    data = leggi_data(data_str) #trasformo la data in oggetto date
    
    cibo = {
        'prodotto': nome_prod,
        'scadenza': data 
    }

    frigorifero.append(cibo)

print("frigorifero attuale", frigorifero)

oggi = datetime.today().date()
for el in frigorifero:
    intervallo_tempo = el['scadenza'] - oggi
    giorni = intervallo_tempo.days
    if  giorni <= 7:
        print(el)
