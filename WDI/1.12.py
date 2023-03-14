# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
def NWD(a,b):
    while b>0:
        a,b=b, a%b
    return a

print(NWD(NWD(600,120),456))