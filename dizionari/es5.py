from datetime import date

ANNO = date.today().year

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# stampare solo i nomi di questa famiglia (usando ciclo)
# calcolare le età di ciascuno

for k in myfamily:
    print(myfamily[k]['name'], ANNO - myfamily[k]['year'], sep=': ')

print("l'età media è: ")
