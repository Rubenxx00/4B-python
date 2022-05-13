# creare un dizionario "alunno1" che contenga:
# nome, classe, voti_inglese, voti_informatica
# e valorizzarlo da input (esattamente 3 voti)

# stampare il dizionario
# calcolare la media di inglese e informatica e stampare il nome della materia in cui va meglio

def media(lista_voti):
    somma = 0
    for el in lista_voti:
        somma += el
    return somma / len(lista_voti)


alunno1 = {
    "nome": "",
    "classe": "",
    "voti_inglese": [],
    "voti_informatica": []
}

alunno1['nome'] = input("inserisci nome alunno")
alunno1['classe'] = input("inserisci classe alunno")

for i in range(3):
    voto = float(input("inserisci il prossimo voto di inglese"))
    alunno1['voti_inglese'].append(voto)

for i in range(3):
    voto = float(input("inserisci il prossimo voto di infomatica"))
    alunno1['voti_informatica'].append(voto)

print(alunno1)

media_informatica = media(alunno1['voti_informatica'])
print(media_informatica)
# stampare primo e ultimo voto di info
print(alunno1['voti_inglese'][0], alunno1['voti_inglese'][-1])
