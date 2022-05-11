# data una lista di parole, contare quante volte è presente ognuna
# ["cane", "gatto", "cane", "topo","cane","topo"]
# cane: 3
# topo: 2
# gatto: 1

li = ["cane", "gatto", "cane", "topo","cane","topo"]

d = {}

for el in li:
    if el in d:
        d[el] = d[el] + 1
    else:
        d[el] = 1

d2 = {}

for el in li:
    d2[el] = d2.get(el, 0) + 1

print(d)
