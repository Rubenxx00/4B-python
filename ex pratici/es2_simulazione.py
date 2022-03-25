'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

Funzione che presa in input una lista, restituisce una nuova lista contenente elementi della prima, senza duplicati
'''

def unique(li):
    unique = []
    for el in li:
        if el not in unique:
            unique.append(el)
    return unique

li = [1,2,3,3,3,3,4,5]
print(unique(li))