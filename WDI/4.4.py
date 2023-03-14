# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

y_2=3
x_2=11
tab=[[n for n in range(1,x_2+1)]for _ in range(0,y_2)]
for d in tab:
    print(d)

najwIloraz=0
wiersz=0
kolumna=0
for y in range(0,y_2):
    for x in range(0,x_2):
        print(y,x, tab[y][x])
        sumaKol=0
        sumaWie=0
        for q in range(0,y_2):
            sumaWie+=tab[q][x]
        for q in range(0,x_2):
            sumaKol+=tab[y][q]
        print(sumaKol,sumaWie)
        if sumaWie/sumaKol>najwIloraz:
            najwIloraz=sumaWie/sumaKol
            wiersz=y
            kolumna=x
print(najwIloraz,wiersz,kolumna)