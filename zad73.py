with open("tekst.txt") as plik:
    tekst = plik.read().strip()

ile = 0
napisy = tekst.split()
for napis in napisy:
    for i in range(len(napis) - 1):
        if napis[i] == napis[i + 1]:
            ile += 1
            break
print(ile)

slownik = {}
for znak in tekst:
    if znak.isalpha():
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1

if 'Z' not in slownik:
    slownik['Z'] = 0

print("Częstotliwość liter:")
lista = sorted(slownik.items())
suma = sum(slownik.values())
for kr in lista:
    print(kr[0], ':', kr[1], round(100 * kr[1] / suma, 2), '%')

samogloski = {'A', 'E', 'I', 'O', 'U', 'Y'}
maks = 0
ileNapisow = 0
for napis in napisy:
    n = 0
    for litera in napis:
        if litera not in samogloski:
            n += 1
            maks = max(maks, n)
        else:
            n = 0
print(maks)

najdluzsze = 0
licznik = 0
odpowiedz = ""
for napis in napisy:
    n = 0
    max_local = 0
    for litera in napis:
        if litera not in samogloski:
            n += 1
            max_local = max(max_local, n)
        else:
            n = 0
    if max_local > najdluzsze:
        najdluzsze = max_local
        licznik = 1
        odpowiedz = napis
    elif max_local == najdluzsze:
        licznik += 1

print(licznik)
print(odpowiedz)
