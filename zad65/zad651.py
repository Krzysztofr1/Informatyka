liczniki = []
mianowniki = []
with open("dane_ulamki.txt", "r") as plik:
    for linia in plik.readlines():
        liczby = linia.split()
        liczniki.append(int(liczby[0]))
        mianowniki.append(int(liczby[1]))


minimalny_ulamek = [liczniki[0], mianowniki[0]]
for i in range(1, len(liczniki)):
    if liczniki[i] * minimalny_ulamek[1] < minimalny_ulamek[0] * mianowniki[i]:
        minimalny_ulamek = [liczniki[i], mianowniki[i]]
    elif liczniki[i] * minimalny_ulamek[1] == minimalny_ulamek[0] * mianowniki[i]:
        if mianowniki[i] < minimalny_ulamek[1]:
            minimalny_ulamek = [liczniki[i], mianowniki[i]]

print(minimalny_ulamek)




