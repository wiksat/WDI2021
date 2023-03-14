import math
T = [2,3,7,8,10,23,15,30]
tab = [0,0,0]
posT=0
posTab=0
def waga(liczba):
    l=liczba
    wag=0
    k=2
    while l>1 and k<=math.sqrt(liczba)+1:
        if l%k==0:
            wag+=1
            while l%k==0:
                l//=k
        k+=1
    if (l != 1): wag += 1
    return wag
def rekur(T):
    global posT
    global posTab
    wag=waga(T[posT])
    if wag not in tab:
        if posTab>3:
            return False
        tab[posTab]=wag
        posTab+=1
    if posT+1<len(T):
        posT+=1
        return rekur(T)
    else:
        if (posTab == 3):
            return True
        else:
            return False
print(rekur(T))