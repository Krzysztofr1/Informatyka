def homer(liczba, x):

    W = int(liczba[0])
    for i in range(1, len(liczba)):
        W = W * x + int(liczba[i])
    return W
with open("liczby2.txt", "r") as file:
    liczby_decimal = list(map(int, file.read().splitlines()))
cyfra_6_decimal = 0
cyfra_6_octal = 0
for liczba in liczby_decimal:
        cyfra_6_decimal += str(liczba).count("6")
        liczba_octal = oct(liczba)[2:]
        cyfra_6_octal += liczba_octal.count("6")


print(cyfra_6_decimal)
print(cyfra_6_octal)

