print("programma per calcolare...")

euro = 2000.0 #float(input("Importo in euro?"))
cambio = 1.13 #float(input("Cambio euro/dollaro?"))
dollari = euro * cambio

print(" " * 16 + "Euro" + "   Cambio" + " " * 14 + "Dollaro")
print(f"{euro:20.2f} {cambio:8.2f} {dollari:20.2f}")

print('{0:^20} {1:^20} {2:^20}'.format("Euro", "Cambio", "Dollari"))
print('{0:^20.2f} {1:^20.2f} {2:^20.2f}'.format(euro, cambio, dollari))
