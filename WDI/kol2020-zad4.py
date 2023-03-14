def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(num ** 0.5) + 3, 6):
        if num % (i + 1) == 0 or num % (i - 1) == 0:
            return False

    return True
def divide(N,i=0,k=1,prod=0,d=4,i2=0):
    print(N,i,k,prod,i2)
    if i==d:

        if is_prime(k) and is_prime(prod):
            print(prod, k)
            return True
        return False
    if is_prime(prod):
        return divide(N//10,i+1,k,prod+((N%10)*(10**i2)),d,i2+1) or divide(N//10,i+1,k+1,(N%10),d,1)
    return divide(N//10,i+1,k,prod+((N%10)*(10**i2)),d,i2+1)
print(divide(2347))