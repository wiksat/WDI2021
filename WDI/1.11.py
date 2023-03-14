# Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

for x in range(1,1000000):
    suma = 0
    for dz in range(1,int(x/2)+1):
        if x%dz==0:
            suma+=dz
    suma2=0
    for dz in range(1,int(suma/2)+1):
        if suma%dz==0:
            suma2+=dz
    if suma2==x and suma!=x:
        print(x, suma)