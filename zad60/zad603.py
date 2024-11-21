def nwd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def znajdz_najwieksza_wzglednie_pierwsza(liczby):
    najwieksza = 0
    for i in range(len(liczby)):
        for j in range(len(liczby)):
            if i != j and nwd(liczby[i], liczby[j]) > 1:
                break
        else:
            if liczby[i] > najwieksza:
                najwieksza = liczby[i]
    return najwieksza
with open("liczby.txt", "r") as plik:
    liczby = list(map(int, plik.readlines()))
    najwieksza = znajdz_najwieksza_wzglednie_pierwsza(liczby)
    print(najwieksza)
