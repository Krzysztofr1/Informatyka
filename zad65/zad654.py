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


b = (2**2) * (3**2) * (5**2) * (7**2) * 13


suma_ulamkow_licznik = 0
for i in range(len(liczniki)):
    suma_ulamkow_licznik += liczniki[i] * (b // mianowniki[i])

print(suma_ulamkow_licznik)
