N = 10
print(f"tavola pitagorica:")
for i in range(1, N+1):
    for j in range(1, N+1):
            n = i*j
            if i==j:
                print(f'({n})\t', end='')
            else:
                print(f'{n}\t', end='') 
                #oppure:
                #print(n, end='\t') 
    # alla nuova riga
    print()
    
    
    
    
    
    
    
        #if i==j:
            #    print(f'({n})\t', end='')
            #else: