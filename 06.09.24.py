def f(x):
    return 2*x-2

def m_z(a,b,e):
    if f(a) * f(b) > 0:
        return None
    while True:
        s=(a+b)/2
        if f(s)==0:
            return s
        if f(a)*f(s)<0:
            b=s
        else:
            a=s
        if abs(b-a)<e:
            return s
print(m_z(0, 10, 0.0001))
