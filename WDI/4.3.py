# Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą.

flaga=True
y=3
x=11
tab=[[n for n in range(1,x+1)]for _ in range(0,y)]
# for x in tab:
#     print(x)


for q in range(0,y):
    flaga2=False
    for w in range(0,x):
        # print(tab[q][w])
        flaga3=False
        while tab[q][w]>0:
            if (tab[q][w]%10)%2==0:
                flaga3=True
                break
            tab[q][w]//=10
        if flaga3:
            flaga2=True
        else:
            flaga2=False
    if flaga2==False:
        flaga==False
print(flaga)