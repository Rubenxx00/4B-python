# esempio di contatore binario a 3 bit
# (cioè visualizza i numeri binari da 0 a 7)
N = 10
for i in range(N):
    for j in range(N):
        for x in range(N):
            print(i, j, x)
    # finito il ciclo interno, stampo un divisore
    print("------")