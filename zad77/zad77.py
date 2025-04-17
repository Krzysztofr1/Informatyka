with open("dokad.txt", "r", encoding="utf-8") as plik:
    tekst = plik.readline().strip()

klucz = "LUBIMYCZYTAC"
wynik = ""
dlugosc_klucza = len(klucz)
indeks_klucza = 0
powtorzenia = 1

for znak in tekst:
    if 'A' <= znak <= 'Z':
        przesuniecie = ord(klucz[indeks_klucza % dlugosc_klucza]) - ord('A')
        kod = ord(znak) + przesuniecie
        if kod > ord('Z'):
            kod -= 26
        wynik += chr(kod)
        indeks_klucza += 1
        if indeks_klucza % dlugosc_klucza == 0:
            powtorzenia += 1
    else:
        wynik += znak

print(powtorzenia)
print(wynik)

with open("szyfr.txt", "r", encoding="utf-8") as plik:
    zaszyfrowany = plik.readline().strip()
    klucz = plik.readline().strip()

wynik = ""
dlugosc_klucza = len(klucz)
indeks_klucza = 0

for znak in zaszyfrowany:
    if 'A' <= znak <= 'Z':
        przesuniecie = ord(klucz[indeks_klucza % dlugosc_klucza]) - ord('A')
        kod = ord(znak) - przesuniecie
        if kod < ord('A'):
            kod += 26
        wynik += chr(kod)
        indeks_klucza += 1
    else:
        wynik += znak

print(wynik)

zliczenia = [0] * 26
for znak in zaszyfrowany:
    if 'A' <= znak <= 'Z':
        zliczenia[ord(znak) - ord('A')] += 1

for i, liczba in enumerate(zliczenia):
    litera = chr(i + ord('A'))
    print(f"{litera}: {liczba}")

suma = sum(zliczenia)
wspolczynnik = sum(c * (c - 1) for c in zliczenia)

if suma > 1:
    ic = wspolczynnik / (suma * (suma - 1))
    szacowana_dlugosc_klucza = 0.0285 / (ic - 0.0385)
    szacowana_dlugosc_klucza = round(szacowana_dlugosc_klucza, 2)
else:
    szacowana_dlugosc_klucza = 0.0

print(szacowana_dlugosc_klucza)
print(len(klucz))

