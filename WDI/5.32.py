def suma(T, k, i=0, sum1=0, count1=0, sum2=0, count2=0):
    if count1+count2==k and sum1==sum2:
        return True
    if len(T)==i:
        return False
    return suma(T,k,i+1,sum1+T[i],count1+1,sum2,count2) or suma(T,k,i+1,sum1,count1,sum2+T[i],count2+1) or suma(T,k,i+1,sum1,count1,sum2,count2)
T=[1,2]
print(suma(T,2))