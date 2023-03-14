# Zadanie 20. Dane są ciągi: An+1 = √An∗Bnoraz Bn+1 = (An+ Bn)/2.0. Ciągi te są zbieżne do
# wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb.
import math

a=4
b=7
for x in range(100):
    a,b=math.sqrt(a*b), (a+b)/2
print(a)
