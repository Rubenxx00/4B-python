nome = input("Nome: ")
cognome = input("Cognome: ")
anno_n = input("Anno nascita: ")
mese_n = int(input("Mese nascita: "))
giorno_n = int(input("Giorno nascita: "))
sesso = input("Sesso: (f/m) ")

cf = nome[:3].upper() + cognome[:3].upper() + anno_n[2:]

cod_ascii_mese = ord('A') - 1 + mese_n # => 64 + mese
cod_mese = chr(cod_ascii_mese)

cf = cf + cod_mese + str(giorno_n)

print(cf)