import math
liczba=int(input())
tab=[]
# for x in range(2,liczba):
#     tab.append(x)
tab = [i for i in range(2,liczba)]
dzielnik=2

while dzielnik<math.sqrt(liczba):
    for x in range(dzielnik - 1, len(tab)):
        if tab[x]%dzielnik==0:
            tab[x]=0
    dzielnik+=1
for x in tab:
    if x>0:
        print(x)
# print(tab)