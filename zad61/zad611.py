ciagi=[]
with open("ciagi.txt","r") as plik:
    for linia in plik.readlines():
        liczby=[]
        for liczba in linia.split():
            liczby.append(int(liczba))

        if len(liczby)>1:
            ciagi.append(liczby)

max=0
roznica=0
liczbaarytmetycznych=0

for c in ciagi:
    roznica=c[1]-c[0]
    for i in range(1,len(c)):
        if c[i]-c[i-1]!=roznica:
            break
    else:
        liczbaarytmetycznych+=1
        if roznica>max:
            max=roznica
print(max)

n=1
szesciany=[]
while n**3 <1000000:
    szesciany.append(n**3)
    n+=1
