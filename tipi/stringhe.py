w = "Palermo"
print(w)
print(w[2])
print(w[-1])
print(w[len(w)-1]) # equivalente alla riga sopra!
print(len(w))

# w[4] = "x" # NB: non è possibile scriverlo in questo modo perchè le stringhe sono immutabili

print(w[4])
"Palexmo"
z = w[:4] + "x" + w[5:]
print(z)

print(z.lower())
print(z.upper())
print(z)
z = z.upper() # da qui in poi z è maiuscola
print(z)