# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An= n ∗n + n + 1.
import math

liczba=9
for x in range(1, int(math.sqrt(liczba)+1)):
    if liczba%(x*x+x+1)==0:
        print("tak")
        break
else:
    print("nie")