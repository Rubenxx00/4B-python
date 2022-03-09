# ulteriori info: https://www.w3schools.com/python/python_casting.asp

età = input("Quanti anni hai? ")

## scrivere codice che calcoli e visualizzi il doppio dell'età chiesta in input

# questo no, perchè età è string
#print(type(età))
#print(età*2)

# versione corretta
età = int(età)
print(type(età))
print(età*2)


















print(int(input("età"))*2)