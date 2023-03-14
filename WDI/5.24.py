import math

def polozenia(T,i=0,sc1=[0,0],sc2=[0,0],s1ile=0,s2ile=0):
    # print(T,i,sc1,sc2,s1ile,s2ile)
    if i==len(T) and s1ile>0 and s2ile>0:
            sc1=[(sc1[0])/s1ile,(sc1[1])/s1ile]
            sc2=[(sc2[0])/s2ile,(sc2[1])/s2ile]
            # print(sc1,s1ile,sc2,s2ile,math.sqrt((sc2[0]-sc1[0])**2+(sc2[1]-sc1[1])**2))
            return True,math.sqrt((sc2[0]-sc1[0])**2+(sc2[1]-sc1[1])**2)
    if i==len(T):
        return False, 9999999999999
    w1=polozenia(T,i+1,[(sc1[0]+T[i][0]),(sc1[1]+T[i][1])],sc2,s1ile+1,s2ile)
    w2=polozenia(T,i+1,sc1,[(sc2[0]+T[i][0]),(sc1[1]+T[i][1])],s1ile,s2ile+1)
    if w1[1]>w2[1]:
        return w2
    else:
        return w1

T=[(0,0),(1,1),(2,2),(3,3)]
print(polozenia(T)[1])