def silnia(n):
    silnia=1
    for x in range(1,n+1):
        silnia*=x
    return silnia
def licz(x):
    mianownik=silnia(x)
    for m in range(0,z+2):
        d=x//mianownik
        tablica[m]+=d
        r=x%mianownik
        r=r*10
        x=r

z=int(input("Podaj dokładność "))
# z=1000
tablica=[0 for i in range(0,z+2)]
for x in range(1,10):
    licz(x)

for x in range(z+1,0,-1):
    if tablica[x]//10>0:
        tablica[x-1]+=tablica[x]//10
        tablica[x]=tablica[x]%10
print(tablica[0],",",end="",sep="")
for x in range(1,z+2):
    print(tablica[x],end="",sep="")