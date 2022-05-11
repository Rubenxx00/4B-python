'''
Scrivi una funzione python che, dato un dizionario e una lista di chiavi, crei e restituisca un nuovo dizionario estraendo le sole chiavi presenti nella lista.
Esempio

Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to extract
keys = ["name", "salary"]

Expected output:
{
    'name': 'Kelly',
    'salary': 8000
}
'''

def estrai(dizionario, chiavi):
    ridotto = {}
    for k in chiavi:
        valore_letto = dizionario[k]
        ridotto[k] = valore_letto
    return ridotto


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to extract
keys = ["jhvvjh", "salary"]

diz = estrai(sample_dict, keys)

print(diz)