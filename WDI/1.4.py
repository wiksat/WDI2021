# Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzy-
# stając z zależności 1 + 3 + 5 + ... = n2.
an=1
r=2
suma=1
liczba=input("Wprowadz liczbe")
ind=1
while suma<liczba:
    ind+=1
    an+=2
    suma += an
if suma==liczba:
    print(ind)