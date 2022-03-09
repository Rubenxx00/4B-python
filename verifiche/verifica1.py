
x = int(input("inserisci la x"))
y = int(input("inserisci la y"))

if x == 0 or y == 0:
    print("è su un asse")
else:
    if y > 0:
        # sopra l'asse delle x
        if x > 0:
            print("primo quadrante")
        else:
            print("secondo quadrante")
    else:
        # sotto l'asse delle x
        if x > 0:
            print("quarto quadrante")
        else:
            print("terzo quadrante")
# altra soluzione
if x==0 or y==0:
    print("il punto è su un'asse")
elif x>0 and y>0:
    print("i numeri si trovano nel primo quadrante")
elif x>0 and y<0:
    print("i numeri si trovano nel quarto quadrante")
elif x<0 and y>0:
    print("i numeri si trovano nel secondo quadrante")
elif x<0 and y<0:
    print("i numeri si trovano nel terzo quadrante")

# quadrato della distanza
x2 = int(input("inserisci la seconda x"))
y2 = int(input("inserisci la seconda y"))

d = (x-x2)**2 + (y-y2)**2
print(d)