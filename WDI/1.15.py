# Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗sqrt(0.5 + 0.5 ∗sqrt(0.5)) ∗sqrt(0.5 + 0.5 ∗sqrt(0.5 + 0.5 ∗
# sqrt(0.5))) ∗... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π
import math

pi=2
ciag=math.sqrt(0.5)
for x in range(100):
    pi=pi/ciag
    ciag=math.sqrt(0.5+0.5*ciag)
print(pi)