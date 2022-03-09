from collections import Counter
import matplotlib.pyplot as plt

# Function to get sum of digits 
def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

# calcola quante volte sarebbe chiamato l'i-esimo alunnno
# numero classi
class_size = 30
# numero pagine del libro
n = 400
c = Counter()
for i in range(1, n+1):
    s = getSum(i)
    while s > class_size:
        s = getSum(s)
    c[s] += 1

# An "interface" to matplotlib
plt.bar(c.keys(), c.values(), color='#0504aa',
                            alpha=0.7)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Alunno')
plt.ylabel('N volte')
plt.title('Istogramma')
plt.show()
