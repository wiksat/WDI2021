# Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + ...
def silnia(w):
    a=1
    for x in range(1,w+1):
        a=a*x
    return a
e=0
for x in range(100):
    e+=1/silnia(x)
print(e)