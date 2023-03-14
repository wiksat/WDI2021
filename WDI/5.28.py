def getOneBin(number):
    i=0
    one=0
    while number>0:
        if number%2==1: one+=1
        number//=2
        i+=1
    return one
def zbior(T, i=0, podz1=0,podz2=0,podz3=0):
    if len(T)==i:
        if podz1==podz2==podz3:
            return True
        else:
            return False
    return zbior(T,i+1,podz1+getOneBin(T[i]),podz2,podz3) or zbior(T,i+1,podz1,podz2+getOneBin(T[i]),podz3) or zbior(T,i+1,podz1,podz2,podz3+getOneBin(T[i]))


T=[2, 3, 5, 7, 15] #True
# T=[5, 7, 15] #False
print(zbior(T))