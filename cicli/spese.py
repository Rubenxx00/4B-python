# spese.py: spese domestiche dell"anno
mesi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug",\
 "Ago", "Set", "Ott", "Nov", "Dic"]

totale = 0
# ripetizione sui mesi
for m in mesi:
 msg = "Spesa mese " + m + ": "
 importo = float(input(msg))
 totale += importo
# output del risultato
print("Spesa annuale: {:12.2f}".format(totale))
