# Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.
import math

liczba=107
flag=True
for x in range(2,int(math.sqrt(liczba)+1)):
    if liczba%x==0:
        flag=False
        break
if flag:
    print("tak")
else:
    print("nie")