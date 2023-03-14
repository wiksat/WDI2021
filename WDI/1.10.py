# Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.

for liczba in range(1,1000000):
    suma=0
    for x in range(1,int(liczba/2)+1):
        if liczba%x==0:
            suma+=x
    if suma==liczba:
        print(liczba)