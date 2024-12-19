def homer(liczba, x):

    W = int(liczba[0])
    for i in range(1, len(liczba)):
        W = W * x + int(liczba[i])
    return W

def decToAll(liczba, system):

    wynik = ""
    while liczba > 0:
        wynik = str(liczba % system) + wynik
        liczba = liczba // system
    return wynik


with open("liczby1.txt", "r") as file:
    liczby_octal = file.read().splitlines()


minimum = 1000000
maximum = 0
min_octal = ""
max_octal = ""


for liczba_octal in liczby_octal:
    liczba_decimal = homer(liczba_octal, 8)
    if liczba_decimal < minimum:
        minimum = liczba_decimal
        min_octal = liczba_octal
    if liczba_decimal > maximum:
        maximum = liczba_decimal
        max_octal = liczba_octal



print(min_octal)
print(max_octal)
