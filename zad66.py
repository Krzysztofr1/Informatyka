def suma_cyfr(liczba):
 s=0
 while liczba:
  s+=liczba%10
  liczba//=10
 return s


def czy_pierwsza(x):
 if x<2:
  return False
 for i in range(2,int(x**0.5)+1):
  if x%i==0:
   return False
 return True


def czy_prostokatny(a,b,c):
 return (a*a+b*b==c*c)or(a*a+c*c==b*b)or(b*b+c*c==a*a)


def czy_trojkat(a,b,c):
 return (a+b>c)and(a+c>b)and(b+c>a)


trojki=[]
with open("trojki.txt") as plik:
 for linia in plik:
  liczby=linia.split()
  if len(liczby)==3:
   a,b,c=map(int,liczby)
   trojki.append((a,b,c))



for a,b,c in trojki:
 if suma_cyfr(a)+suma_cyfr(b)==c:
  print(a,b,c)



for a,b,c in trojki:
 if a*b==c and czy_pierwsza(a) and czy_pierwsza(b):
  print(a,b,c)



poprzedni_ok=False
poprzednia=None
for a,b,c in trojki:
 aktualny_ok=czy_prostokatny(a,b,c)
 if poprzedni_ok and aktualny_ok:
  print(poprzednia[0],poprzednia[1],poprzednia[2])
  print(a,b,c)
  print()
 poprzedni_ok=aktualny_ok
 poprzednia=(a,b,c)


licznik_trojkat=0
aktualny_ciag=0
najdluzszy_ciag=0
for a,b,c in trojki:
 if czy_trojkat(a,b,c):
  licznik_trojkat+=1
  aktualny_ciag+=1
  if aktualny_ciag>najdluzszy_ciag:
   najdluzszy_ciag=aktualny_ciag
 else:
  aktualny_ciag=0



print(licznik_trojkat)
print(najdluzszy_ciag)
