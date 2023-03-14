import math
# def pierw(l):
#     if l==1:
#         return False
#     for dz in range(2, int(math.sqrt(l) + 1)):
#         if l % dz == 0:
#             return False
#     return True
#
# print(pierw(1.5))
#
#
# def is_prime(n):
#     if(n is not int): return False
#     if n == 2 or n == 3: return True
#     if n<=1 or n%2 == 0 or n%3 == 0: return False
#     k = 5
#     while k <= int(math.sqrt(n)) + 1 :
#         if(n%k == 0): return False
#         k+=2
#         if (n % k == 0): return False
#         k+=4
#     return True
# print(is_prime(1.5))

def wytnij(l,i):
    copyL=l
    new=0
    new=copyL//(10**(i+1))
    new*=10**(i)
    new+=copyL%(10**i)
    return new
print(wytnij(123,2))