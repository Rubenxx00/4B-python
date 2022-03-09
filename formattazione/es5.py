teoria = int(input("inserisci il voto di teoria "))
laboratorio = int(input("inserisci il voto di laboratorio "))

individuale = input("inserisci il voto di individuale ")
individuale = int(individuale)

punteggio = (teoria*20 + laboratorio*50 + individuale*30)/100
print(punteggio)

voto = punteggio/10
print(voto)