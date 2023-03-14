# a=str(input())
# b=str(input())
# taba=[]
# tabb=[]
# for znak in a:
#     print(znak)
#     taba.append(znak)
# for znak in b:
#     tabb.append(znak)
# taba.sort()
# tabb.sort()
# # print(taba,tabb)
# print(taba==tabb)

a = int(input())
b = int(input())

digits = [0]*10

while a>0:
    liczba=a%10
    digits[liczba]+=1
    a//=10
while b>0:
    liczba = b % 10
    digits[liczba] -= 1
    b //= 10

for i in range(10):
    if digits[i] != 0:
        print("NIE")
        break
else:
    print("TAK")