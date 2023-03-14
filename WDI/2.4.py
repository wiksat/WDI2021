import math

licznik=0
n=int(input())
for a in range(0,math.ceil(math.log2(n))+1):
    for b in range(0,math.ceil(math.log(n,3))+1):
        for c in range(0, math.ceil(math.log(n, 5)) + 1):
            if ((2**a)*(3**b)*(5**c)<=n):
                print((2**a)*(3**b)*(5**c),a,b,c)