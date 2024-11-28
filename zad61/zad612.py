with open("ciagi.txt", "r") as f:
    ciagi = f.readlines()

wyniki = []
for ciagn in ciagi:
    liczby = map(int, ciagn.split())
    szesciany = [liczba for liczba in liczby if round(liczba ** (1/3)) ** 3 == liczba]
    if szesciany:
        wyniki.append(str(max(szesciany)))

print(wyniki)


