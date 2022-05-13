import requests
from matplotlib import pyplot as plt

URL = "https://www.gutenberg.org/cache/epub/45334/pg45334.txt"

testo = requests.get(URL).text

d = {}

for parola in testo.split(" ")[355:]:
    if len(parola) > 1 and parola.isalnum():
        parola = parola.lower()
        d[parola] = d.get(parola, 0) + 1

filtered = {k: v for k, v in sorted(d.items(), key=lambda item: item[1]) if v > 10}
print(filtered)

print(filtered['lucia'])
