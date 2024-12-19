def homer(liczba, x):
    W = int(liczba[0])
    for i in range(1, len(liczba)):
        W = W * x + int(liczba[i])
    return W


with open("liczby1.txt", "r") as plik1, open("liczby2.txt", "r") as plik2:
    liczby1 = plik1.read().splitlines()
    liczby2 = plik2.read().splitlines()

    liczba_takich_samych = 0
    liczba_wiekszych = 0

    for liczba1, liczba2 in zip(liczby1, liczby2):
        wartosc1 = homer(liczba1, 8)
        wartosc2 = int(liczba2)
        if wartosc1 == wartosc2:
            liczba_takich_samych += 1
        elif wartosc1 > wartosc2:
            liczba_wiekszych += 1


print(liczba_takich_samych)
print(liczba_wiekszych)


