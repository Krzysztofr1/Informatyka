def f(x):
    return x*x+1

def calka(a,b,E):
    p = 0
    x = (b - a) / E
    for i in range(E):
        y=f(a+i*x)
        p+=y*x
    return p



print(calka(0,4,1000))