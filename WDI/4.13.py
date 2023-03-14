import math
def pierw(l):
    print(l)
    if l==1:
        return False
    for dz in range(2,int(math.sqrt(l)+1)):
        if l%dz==0:
            return False
    return True

t = [[60, 60],
     [60, 60]]
n=2
for a in range(n*n):
    zm = False
    for b in range(n*n):
        if t[b//n][b%n]!=0 and a!=b and pierw(t[a//n][a%n]+t[b//n][b%n]):
            zm=True
            break
    if zm==False:
        t[a//n][a%n]=0
for x in t:
    print(x)