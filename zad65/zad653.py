def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


liczniki = []
mianowniki = []
with open("dane_ulamki.txt", "r") as plik:
    for linia in plik.readlines():
        liczby = linia.split()
        liczniki.append(int(liczby[0]))
        mianowniki.append(int(liczby[1]))


suma_licznikow = 0
for i in range(len(liczniki)):
    d = nwd(liczniki[i], mianowniki[i])
    suma_licznikow += liczniki[i] // d

print(suma_licznikow)