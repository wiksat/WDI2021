def nwd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def Nwdz3(a,b,c):
    # return nwd(nwd(a,b),c)
    return nwd(a,b)==1 and nwd(a,c)==1 and nwd(b,c)==1

def rek(t,i=0,wzietych=0,r=[],przerwa=0):
    if wzietych==3:
        if Nwdz3(r[0],r[1],r[2]):
            print(r)
            return 1
        return 0
    if i==len(t):
        return 0
    w=0
    if przerwa==0:
        w=rek(t,i+1,wzietych,r,przerwa)+rek(t,i+1,wzietych+1,[*r,t[i]],2)
    if przerwa==2:
        w+= rek(t, i + 1, wzietych, r, 1) + rek(t, i + 1, wzietych + 1, [*r, t[i]], 2)
    if przerwa==1:
        w += rek(t, i + 1, wzietych + 1, [*r, t[i]], 2)

    return w

# print(rek([2,3,4,6,7,8,10]))
# print(rek([2,4,6,7,8,10,12]))
# print(rek([2,4,3,6,5]))
print(rek([2,3,4,5,6,8,7]))