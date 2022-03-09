a=int(input("immetti il numero"))
if(a<0):
    print("il numnero è negativo")
else:
    b="il numero  "

    if(a%2==0):
        b+="è divisibile per 2 "
    else:
        b+="non è divisibile per 2 "

    if(a%3==0):
        b+="ed è divisibile per 3 "
    else:
        b+="ma non è divisibile per 3 "

    if(a%4==0):
        b+="ed è divisibile per 4"
    else:
        b+="ma non è divisibile per 4"
    
    print(b)