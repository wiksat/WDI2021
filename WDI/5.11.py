def rek(t,iloczynTarget,iloczyn=1,count=0,i=0):
    if iloczynTarget==iloczyn:
        return True, count
    if len(t)==i:
        return False,0
    tmp1=rek(t,iloczynTarget,iloczyn*t[i],count+1,i+1)
    tmp2=rek(t,iloczynTarget,iloczyn,count,i+1)
    if tmp1[1] > tmp2[1]:
        return tmp1
    else:
        return tmp2


t=[4,4,2,2,2,2]
print(rek(t,16)[1])
