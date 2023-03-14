# Zadanie 9. Napisać program wypisujący podzielniki liczby.
import math

liczba=100
for x in range(1,int(liczba/2)+1):
    if liczba%x==0:
        print(x)