""" funzione che stampa i numeri da 0 a 16, eccetto il 7 ed il 16

funzione che stampa i numeri da 0 a 16, eccetto:
  i multipli di 7
  ed il 16


...poi programma che chiami le funzioni """

def stampa_1():
    for i in range(16): # mi ricordo che il 16 è già escluso
        if i == 7:
            continue
        print(i, end=" ")
    print()

def stampa_2():
    for i in range(16): # mi ricordo che il 16 è già escluso
        if i % 7 == 0:
            continue
        print(i, end=" ")
    print()


stampa_1()
stampa_2()


