# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe
import math
def pierw(l):
    wynik=0
    c=1
    while l > 0:
        wynik+=(l%10)*c
        l//=10
        c+=1
    x=1
    for dz in range(2,int(math.sqrt(wynik)+1)):
        if wynik%dz==0:
            return False
    return True

def rek(T,poz,ciag,flag):
    # print(T,poz,ciag,flag)
    if flag and poz>=len(T):
        if ciag >=10 and pierw(ciag):
            return True
        else:
            return False
    if poz>=len(T):
        return False
    else:
        if pierw(ciag) and ciag >=10:
            # print("wykonało sie")
            return rek(T,poz+1,ciag*10+T[poz],False) or rek(T,poz+1,T[poz],True)
        return rek(T,poz+1,ciag*10+T[poz],flag)
T = [1, 1, 1, 0, 1, 1]
# T=[1,1,0,1,0,0]
print(rek(T,0,0,False))