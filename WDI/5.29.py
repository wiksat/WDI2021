import math

def punkt(T, r,i=0,used=[],iUsed=0):
    if iUsed==3:
        if math.sqrt(math.sqrt((T[used[0]][0]+T[used[1]][0]+T[used[2]][0])**2+(T[used[0]][1]+T[used[1]][1]+T[used[2]][1])**2)**2+(T[used[0]][2]+T[used[1]][2]+T[used[2]][2])**2)<=r:
            return True
        else:
            return False
    if i==len(T):
        return False
    return punkt(T, r,i+1,[*used,i],iUsed+1) or punkt(T, r,i+1,used,iUsed)



T=[(2,3,4),(53.4,6,3),(7.3,55,0),(3,4,5),(3,4,5),(6,7,8)]
print(punkt(T,20))