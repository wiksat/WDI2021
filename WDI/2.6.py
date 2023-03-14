# Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
# o najmniejszej różnicy. Np. 30 = 5 ∗6, 120 = 10 ∗12.
import math

# liczba=5644
liczba=int(input("Podaj liczbę: "))
temp=int(math.sqrt(liczba))
while temp>=1:
    if liczba%temp==0:
        print(temp,liczba/temp)
        break
    temp-=1