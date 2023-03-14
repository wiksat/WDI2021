import math


def isNotPrime(liczba):
    dec=0
    c = 1
    while liczba > 0:
        dec += c * (liczba % 10)
        liczba //= 10
        c *= 2
    liczba=dec
    for x in range(2,int(math.sqrt(liczba)+1)):
        if liczba%x==0:
            return True
    return False

def liczby(a,b,prod=""):
    if a==0 and b==0:
        if prod[0]=="1" and isNotPrime(int(prod)):
            return 1
        else:return 0
    suma=0
    if a>0:
        suma+=liczby(a-1,b,prod+"1")
    if b>0:
        suma+=liczby(a,b-1,prod+"0")
    return suma

print(liczby(2,3))