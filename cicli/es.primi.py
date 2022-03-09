n=int(input('inserisci valore: '))
conta=0

for i in range(1,n+1):
    if n%i==0:
        conta+=1

if conta==2:
    print(f'sappi che il numero {n} è primo')
else:
    print(f'sappi che il numero {n} non è primo')
