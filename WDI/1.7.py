# Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
liczba=40
m=1
n=0
while m*n<liczba:
    m,n=m+n,m
if m*n==liczba:
    print("tak")
else:
    print("nie")