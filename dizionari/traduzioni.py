# carico il dizionario
ita_to_eng = {
    "lunedì": "monday",
    "martedì": "tuesday",
    "mercoledì": "wednesday"
}

# "invertire" il dizionario
eng_to_ita = {}

for k in ita_to_eng:
    inglese = ita_to_eng[k] # monday, ...
    eng_to_ita[inglese] = k

print(eng_to_ita)
