# Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.


liczba=2
a=1
b=liczba
while abs(a-b)>0.00001:
    a=(a+b)/2
    b=liczba/a

print(a)
