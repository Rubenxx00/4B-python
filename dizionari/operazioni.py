d = {1: 'Blue', 2: 'Pink'}
print(d)

d[1] = 'Yellow'
print(d)

d[3] = 'Black'
print(d)

del d[3] # elimino la coppia chiave-valore con chiave 3
print(d)

d.clear()
print(d) # dizionario vuoto


# creare un dizionario che contenga i dati personali di un alunno, chiedendo in input nome, cognome, codice fiscale, anno nascita (magari funzione che, dato un dizionario restituisca l'età)
# se è maggiorenne, chiedere e inserire nel dizionario il numero della patente
# altrimenti cancellare il cod fiscale

from datetime import date

def età(alunno):
    nascita = alunno['anno nascita']
    anno_corrente = date.today().year
    return anno_corrente - nascita

alunno = {}

alunno['nome'] = input("nome: ")
alunno['cognome'] = input("cognome: ")
alunno['cf'] = input("cod fiscale: ")
alunno['anno nascita'] = int(input("anno nascita: "))

if età(alunno) >= 18:
    alunno['patente'] = input("cod patente: ")
else:
    #alunno.pop('cf')
    del alunno['cf']

print(alunno)

if 'patente' in alunno:
    print('è stata caricata la patente')
else:
    print('non è stata caricata la patente')

# metodo genera dizionario from keys
chiavi = ['nome', 'cognome']
diz = {}.fromkeys(chiavi, 0)
print(diz)
