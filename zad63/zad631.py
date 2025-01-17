
def czy_dwucykliczny(ciag):
    dlugosc = len(ciag)

    if dlugosc % 2 != 0:
        return False

    polowa = dlugosc // 2
    return ciag[:polowa] == ciag[polowa:]


with open("ciagi.txt", "r") as plik:
    ciagi = [linia.strip() for linia in plik]



for ciag in ciagi:
    if czy_dwucykliczny(ciag):
        print(ciag)
