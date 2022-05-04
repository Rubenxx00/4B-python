# Write a Python function to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*3).
# Then, print its values list and its keys list.
# If any value is greater than 100, print it.
# Finally print the dictionary element by element in the form. Expected output:
# 1 -> 1
# 2 -> 8
# 3 -> 27

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

def genera_dizionario(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i**3
    return d

diz = genera_dizionario(5)
print("chiavi")
print(diz.keys())

print("\nvalori")
print(diz.values())

print("\nvalori maggiori di 100")
for v in diz.values():
    if v > 100:
        print(v)

for k in diz.keys():
    print(f"il cubo di {k} è {diz[k]}")

for k in diz.keys():
    print(str(k) + '->' + str(diz[k]))
    # oppure
    # print(f'{k} -> {diz[k]}') 