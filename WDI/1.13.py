# Zadanie 13. Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

def NWD(a,b):
    while b>0:
        a,b=b, a%b
    return a

a=120
b=605
d=a*b/NWD(a,b)
print(d)