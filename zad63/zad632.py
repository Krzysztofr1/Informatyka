def brak_sasiadujacych_jedynek(ciag):
    for i in range(len(ciag) - 1):
        if ciag[i] == '1' and ciag[i + 1] == '1':
            return False
    return True

with open("ciagi.txt", "r") as plik:
    ciagi = [linia.strip() for linia in plik]

liczba_ciagow = sum(1 for ciag in ciagi if brak_sasiadujacych_jedynek(ciag))

print(liczba_ciagow)