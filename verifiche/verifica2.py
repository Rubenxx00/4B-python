s = input("inserisci la stringa")

if len(s) % 2 == 0:
    s = s[:-3] + s[-3:].upper()
else:
    s = s[:2].upper() + s[2:]

s2 = input("inserisci la seconda stringa")

s = s + " " + s2

print(f"La stringa {s} è lunga {len(s)}")
print("La stringa", s, "è lunga", len(s))
print("La stringa {0:s} è lunga {1:d}".format(s, len(s)))
