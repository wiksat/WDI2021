tab=[0]*10
while True:
    n=int(input())
    if n==0:
        print(tab[9])
        break
    for i in range(10):
        if n>tab[i]:
            n,tab[i]=tab[i],n
    print(tab)