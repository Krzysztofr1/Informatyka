lista=[]
with open("liczby.txt","r") as plik:
    for linia in plik.readlines():
        lista.append(int(linia))
licznik=0
l1=0
l2=0
for i in lista:

    if i<1000:
        licznik+=1
        l1=l2
        l2=i
print(l1,l2,licznik)

