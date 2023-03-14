def rek(t,iloczynTarget,iloczyn=1,count=0,i=0,flag=False,enki=[]):
    if iloczynTarget==iloczyn and flag:
        print(enki)
        return 1
    if len(t)==i:
        return 0
    suma=0
    suma+=rek(t,iloczynTarget,iloczyn*t[i],count+1,i+1,True,[*enki,t[i]])
    suma+=rek(t,iloczynTarget,iloczyn,count,i+1, flag,enki)
    return suma


t=[4,4,2,2,2,2]
print(rek(t,16))
