import random

# genero 100 numeri casuali in modo equivalente
for i in range(100):
    r = random.random()
    r = int(r*100) % 50 # numeri da 0 a 50 (escluso)
    print(r)

for i in range(100):
    r = random.randint(0, 50)
    print(r)

