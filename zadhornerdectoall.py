def homer(liczba,x):
    W=int(liczba[0])
    for i in range(1,len(liczba)):
        W=W*x+int(liczba[i])
    return W




def decToAll(liczba,system):
    wynik=""
    while liczba>0:
        wynik = str(liczba%system)+wynik
        liczba=liczba//system
    return wynik

print(decToAll(26,2))