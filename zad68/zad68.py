lista_wyrazow = []
with open("dane_napisy.txt", "r") as plik:
    for linia in plik:
        lista_wyrazow.append(linia.split())

licznik_68_1 = 0
for wyrazy in lista_wyrazow:
    if len(wyrazy[0]) == len(wyrazy[1]):
        if len(set(wyrazy[0])) == 1 and len(set(wyrazy[1])) == 1 and wyrazy[0] == wyrazy[1]:
            licznik_68_1 += 1
print(licznik_68_1)

licznik_68_2 = 0
for wyrazy in lista_wyrazow:
    if sorted(wyrazy[0]) == sorted(wyrazy[1]):
        licznik_68_2 += 1
print(licznik_68_2)

c1 = [None] * 1000
c2 = [None] * 1000
for i in range(1000):
    t1 = [0] * 10
    t2 = [0] * 10
    for litera in lista_wyrazow[i][0]:
        t1[ord(litera) - ord('A')] += 1
    for litera in lista_wyrazow[i][1]:
        t2[ord(litera) - ord('A')] += 1
    c1[i] = t1
    c2[i] = t2

max_powt = 0
for i in range(1000):
    ile_powt = 0
    for j in range(1000):
        if c1[i] == c1[j]:
            ile_powt += 1
        if c1[i] == c2[j]:
            ile_powt += 1
    if ile_powt > max_powt:
        max_powt = ile_powt

    ile_powt = 0
    for j in range(1000):
        if c2[i] == c1[j]:
            ile_powt += 1
        if c2[i] == c2[j]:
            ile_powt += 1
    if ile_powt > max_powt:
        max_powt = ile_powt

print(max_powt)
