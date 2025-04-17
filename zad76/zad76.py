with open('szyfr1.txt') as plik:
    linie = plik.read().splitlines()
    napisy = linie[:6]
    klucz = list(map(int, linie[6].split()))

wyniki = []
for napis in napisy:
    napis = list(napis)
    for i in range(50):
        a, b = i, klucz[i] - 1
        napis[a], napis[b] = napis[b], napis[a]
    wyniki.append(''.join(napis))

for wynik in wyniki:
    print(wynik + "\n")

with open('szyfr2.txt') as plik:
    linie = plik.read().splitlines()
    napis = linie[0]
    klucz = list(map(int, linie[1].split()))

napis = list(napis)
dlugosc = len(klucz)
for i in range(len(napis)):
    a, b = i, klucz[i % dlugosc] - 1
    napis[a], napis[b] = napis[b], napis[a]

print(''.join(napis))

with open('szyfr3.txt') as plik:
    napis = plik.read().strip()

klucz = [6, 2, 4, 1, 5, 3]
napis = list(napis)
dlugosc = len(klucz)
for i in range(49, -1, -1):
    a, b = i, klucz[i % dlugosc] - 1
    napis[a], napis[b] = napis[b], napis[a]

print(''.join(napis))
