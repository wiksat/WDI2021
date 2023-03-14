# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona
m=1
n=0
while n<1000000:
    m,n=m+n,m
    print(n)