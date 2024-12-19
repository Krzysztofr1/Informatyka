def homer(liczba, x):

    W = int(liczba[0])
    for i in range(1, len(liczba)):
        W = W * x + int(liczba[i])
    return W


with open("liczby2.txt", "r") as file:
    liczby_decimal = list(map(int, file.read().splitlines()))

naj_dlugosc_podciagu = 0
naj_pierwszy = None
poprzednia = 1000000
dlugaosc_podciagu = 0
pierwszy = None

for liczba in liczby_decimal:
    if liczba < poprzednia:
        if dlugaosc_podciagu > naj_dlugosc_podciagu:
            naj_dlugosc_podciagu = dlugaosc_podciagu
            naj_pierwszy = pierwszy
        pierwszy = liczba
        dlugaosc_podciagu = 1
    else:
        dlugaosc_podciagu += 1
    poprzednia = liczba


if dlugaosc_podciagu > naj_dlugosc_podciagu:
    naj_dlugosc_podciagu = dlugaosc_podciagu
    naj_pierwszy = pierwszy


print(naj_pierwszy,naj_dlugosc_podciagu)


