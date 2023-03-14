import math
def pierw(l):
    print(l)
    for dz in range(2,int(math.sqrt(l)+1)):
        if l%dz==0:
            return False
    return True


def liczby(l1,l2,t=""):
    if l1==0 and l2==0:
        if pierw(int(t)):
            return 1
        else:
            return 0
    suma=0
    if l1>0:
        suma+=liczby(l1//10,l2,str(l1%10)+t)
    if l2>0:
        suma+=liczby(l1,l2//10,str(l2%10)+t)
    return suma

print(liczby(13,1))
print(liczby(123,75))