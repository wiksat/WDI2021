# Zadanie 16. Dany jest ciąg określony wzorem: An+1 = (Anmod2) ∗(3 ∗An+ 1) + (1 −Anmod2) ∗An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.


max_a1=0
max_kroki=0
for x in range(2,10001):
    kroki=0
    an=x
    while an>1:
        an = (an % 2) * (3 * an+ 1) + (1 - an % 2) * an / 2
        kroki+=1
    if max_kroki<kroki:
        max_kroki=kroki
        max_a1=x

print(max_a1)