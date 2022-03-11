import matplotlib.pyplot as plt

def plot(n0, n1):
    r = n1/n0
    a = 360/(r+1)
    sizes = [360-a, a]
    explode = (0, 0.1)  # only "explode" the 2nd slice
    labels=[n1, n0]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, startangle=90, labels=labels)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def fibonacci_generico(n, n0, n1): # rendo parametrico n0, n1
    print(n0, end=" ")
    print(n1, end=" ")
    for i in range(n-2):
        x = n0 + n1
        print(x, end=" ")
        n0 = n1
        n1 = x
        plot(n0, n1)

def fibonacci(n):
    fibonacci_generico(n, 0, 1)

def sequenza_di_rossi(n):
    fibonacci_generico(n, 5, 6)

def sequenza_utente(n):
    nome = input("inserisci il tuo nome: ")
    x = int(input("inserisci il primo numero della sequenza: "))
    y = int(input("inserisci il seconda numero della sequenza: "))
    print(f"sequenza di {nome}")
    fibonacci_generico(n, x, y)

sequenza_utente(10)
