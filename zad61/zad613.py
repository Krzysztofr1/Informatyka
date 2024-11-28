with open("bledne.txt", "r") as f:
    ciagi = f.readlines()
wyniki = []
for ciagn in ciagi:
    liczby = list(map(int, ciagn.split()))
    dlugosc = len(liczby)
    if dlugosc < 4:
        continue
    roznice = [liczby[i + 1] - liczby[i] for i in range(dlugosc - 1)]
    if roznice[0] != roznice[1] and roznice[1] == roznice[2]:
        wyniki.append(str(liczby[0]))
        continue
    if roznice[0] != roznice[2] and roznice[1] != roznice[2] and roznice[2] == roznice[3]:
        wyniki.append(str(liczby[1]))
        continue
    for i in range(dlugosc - 1):
        if roznice[i] != roznice[0]:
            wyniki.append(str(liczby[i + 1]))
            break
print(wyniki)

