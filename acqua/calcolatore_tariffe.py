# costanti in maiuscolo
ALIQUOTA = 10
LIMITE_1S = 80
PREZZO_1S = 0.30
PREZZO_2S = 0.35
QUOTA_PRIVATI = 10
QUOTA_AZIENDE = 20

# TODO: aggiungere secondo scaglione, consumi oltre LIMITE_1S, prezzo unitario 0.40.
# modificare i calcoli!

# eccetera...

# nota: calcoli semplificati
def calcola_privati(consumo):
    totale = _calcolo_importo_base(consumo)
    totale += QUOTA_PRIVATI
    totale = totale + (totale*ALIQUOTA/100)
    return totale

def calcola_aziende(consumo):
    totale = _calcolo_importo_base(consumo)
    totale += QUOTA_AZIENDE
    totale = totale + (totale*ALIQUOTA/100)
    return totale
    
# funzione ad uso interno del modulo!
def _calcolo_importo_base(consumo):
    totale = 0
    if consumo > LIMITE_1S:
        totale = (LIMITE_1S * PREZZO_1S) + ((consumo - LIMITE_1S) * PREZZO_2S)
    else:
        totale = consumo * PREZZO_1S
    # metodo alternativo
    totale = min(LIMITE_1S, consumo) * PREZZO_1S + max((consumo - LIMITE_1S), 0) * PREZZO_2S
    return totale