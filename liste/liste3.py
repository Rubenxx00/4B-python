# carichiamo da codice una lista di interi "casuali", sostituire la prima occorrenza del numero 40 con il quadrato di 40

li=[10,20,30,50,60,70,80]
print(li)

i40 = li.index(40)

if 40 in li:
    i40 = li.index(40)
    li[i40] = 40**2
    print(li)

print("fine")