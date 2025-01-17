import math


def czy_pierwsza(x):
    if x <2:
        return False
    if x %2 ==0 and x!=2:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x%i== 0:
            return False
    return True


def czy_polpierwsza(x):
    if czy_pierwsza(x):
        return False
    if x %2==0:
        return czy_pierwsza(x// 2)
    for j in range(3, int(math.sqrt(x)) + 1, 2):
        if x%j == 0:
            return czy_pierwsza(j) and czy_pierwsza(x// j)
    return False

def bin2wart(bin):
    return int(bin, 2)

with open("ciagi.txt", "r") as plik:
    ciagi = [linia.strip() for linia in plik]


polpierwsze = []
for ciag in ciagi:
    liczba = bin2wart(ciag)
    if czy_polpierwsza(liczba):
        polpierwsze.append(liczba)

min_polpierwsza = min(polpierwsze)
max_polpierwsza = max(polpierwsze)

print(len(polpierwsze))
print(min_polpierwsza)
print(max_polpierwsza)
