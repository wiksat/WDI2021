import math


def zamiana(liczba,system):
    nowa_liczba=[]
    chars=[str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("F")+1)]
    while liczba>0:
        nowa_liczba.append(chars[liczba%system])
        liczba//=system
    # print(nowa_liczba)
    return "".join(nowa_liczba[::-1])

def zamiana2(liczba,system):
    digits="0123456789abcdef"
    d1=int(math.log(liczba,system))+1 #dlugosc zapisu w danym systemie
    res=['0']*d1
    print(res)
    for i in range(d1):
        d=liczba%system
        res[-(i+1)]=digits[d]
        liczba//=system
    return res


liczba=int(input())
system=int(input())
print(zamiana(liczba,system))
print(zamiana2(liczba,system))
# print(chars)