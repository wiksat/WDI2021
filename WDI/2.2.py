# a = 73
# b = 6
# n = 2
# dzielesb = a//b
# first = dzielesb
# reszta = a%b
# zapis = 0
# for i in range(0,n):
#     dzielesb = reszta * 10
#     dzielesb, reszta = dzielesb // b, dzielesb%b
#     zapis = zapis*10 + dzielesb
# wynik = first + zapis / 10**n
# print(wynik)

a = int(input())
b = int(input())
n = int(input())

print(a//b, "." if n>0 else "" , sep="", end="")
a %= b
while n > 0:
    a *= 10
    print(a//b, end="")
    a %= b
    n -= 1