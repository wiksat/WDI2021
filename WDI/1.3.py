# Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
# sumie.
m=1
n=0
m2=1
n2=0
zadana_suma=9
suma=0
while zadana_suma!=suma:
    while suma<zadana_suma:
        m,n=m+n,m
        suma+=n

    while suma>zadana_suma:
        m2,n2=m2+n2,m2
        suma-=n2
    if n==n2:break

if suma==zadana_suma:
    print("tak")
else:
    print("nie")