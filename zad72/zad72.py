with open("napisy.txt") as plik:
    dane = [linia.strip().split() for linia in plik]


licznik = 0
pierwsza_para = None
for a, b in dane:
    if len(a) >= 3 * len(b) or len(b) >= 3 * len(a):
        licznik += 1
        if pierwsza_para is None:
            pierwsza_para = (a, b)
print(licznik)
print(pierwsza_para)


znalezione = False
for a, b in dane:
    if len(a) < len(b) and b.startswith(a):
        dopisane = b[len(a):]
        print(a, b, dopisane)
        znalezione = True


max_dlugosc = 0
pary = []
for a, b in dane:
    min_dlugosc = min(len(a), len(b))
    dlugosc = 0
    for i in range(1, min_dlugosc + 1):
        if a[-i] != b[-i]:
            break
        dlugosc += 1
    if dlugosc > max_dlugosc:
        max_dlugosc = dlugosc
        pary = [(a, b)]
    elif dlugosc == max_dlugosc and dlugosc > 0:
        pary.append((a, b))
print(max_dlugosc)
for a, b in pary:
    print(a, b)
