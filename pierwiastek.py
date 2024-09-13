
def pierwiastek(p,e):
    a=1
    a_p=p
    while abs(a-a_p)>e:
        a=(a+a_p)/2
        a_p=p/a

    return a


print(pierwiastek(9,0.00000001))
