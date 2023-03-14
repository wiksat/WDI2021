import math
def pierw(n):
    czynniki = [0]*20
    # print(czynniki)
    k = 2
    c=0
    while n != 1:
        while n % k == 0:
            n //= k
            if k not in czynniki:
                czynniki[c]=k
                c+=1
        k += 1
    # print(czynniki)
    return czynniki
def sum_ilo(tab,product=1 , i=0):
    if i==len(tab) or tab[i]==0:
        return product
    suma=0
    suma+=sum_ilo(tab,product*tab[i],i+1)
    suma += sum_ilo(tab, product, i + 1)
    return suma



tab=pierw(60)
ile=len(tab)
print(sum_ilo(tab)-1)