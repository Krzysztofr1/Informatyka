with open("liczby.txt", "r") as plik:
    linie = plik.readlines()
    liczby = [int(linia) for linia in linie]

def znajdz_dzielniki(a):
    dzielniki = []
    for i in range(1, a + 1):
        if a % i == 0:
            dzielniki.append(i)

    if len(dzielniki) == 18:
        print(a)
        print(dzielniki)

for liczba in liczby:
    znajdz_dzielniki(liczba)

