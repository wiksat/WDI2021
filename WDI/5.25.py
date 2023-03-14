def czynNat(liczba):
    liczbaC=liczba
    w=0
    cz=2
    while liczba>1:
        if liczba%cz==0:
            w=cz
            liczba/=cz
        else:cz+=1
    if w!=liczbaC:
        return w
    else:
        return 0
def skok(t,k=0,ni=0):
    print(t,k,ni)
    if ni==len(t)-1:
        return True,k
    if ni > len(t):
        return False,-1
    if czynNat(t[ni])==0:
        return False,-1
    else:
        return skok(t,k+1,ni+czynNat(t[ni]))
t=[10,4,3,2,3,4,8,6]
print(skok(t)[1])

