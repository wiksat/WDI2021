# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku
suma = 10000
best = (2021, 0)

for i in range(2022):
    m = 2021
    n = i
    while n > 0 and m > n:
        n, m = m-n, n
    if n + m < suma:
        suma = n + m
        best = (n, m)

print(suma, best)