# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.
flaga=True
y=3
x=11
tab=[[n for n in range(1,x+1)]for _ in range(0,y)]
# for d in tab:
#     print(d)

najwIloraz=0
wiersz=0
kolumna=0
for y in range(0,y):
    for x in range(0,x):
        print(y,x)
        sumaKol=0
        sumaWie=0
        xCopy=x
        yCopy=y
        while xCopy>=0:
            sumaKol=sumaKol+tab[y][xCopy]
            xCopy-=1
        while yCopy>=0:
            sumaWie=sumaWie+tab[yCopy][x]
            yCopy-=1
        # print(sumaKol,sumaWie)
        if sumaKol!=0 and sumaWie!=0:
            if sumaKol/sumaWie>najwIloraz:
                najwIloraz=sumaKol/sumaWie
                wiersz=y
                kolumna=x
# print(najwIloraz,wiersz,kolumna)