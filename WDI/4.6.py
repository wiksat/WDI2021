T1=[[1,5,8,9],
    [3,4,5,6],
    [1,2,3,4],
    [2,6,60,66]]
m=0
for a in T1:
    if max(a)>m:
        m=max(a)
        # print(m)
pom=[0]*(m+1)
for y in range(len(T1)):
    for x in range(len(T1)):
        # print(T1[y][x])
        pom[T1[y][x]]+=1
T2=[0]*(len(T1)**2)
poz=0
for i in range(len(pom)):
    if pom[i]==1:
        T2[poz]=i
        poz+=1
print(T2)