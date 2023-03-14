def rek(T, zadana, zastepcza, i, j):
    if i > 3:
        return False
    if zastepcza == zadana and i == 3:
        return True
    if j == len(T):
        return False
    if T[j] == 0:
        if rek(T, zadana, zastepcza + T[j], i+1, j+1) or rek(T, zadana, zastepcza, i, j+1):
            return True
    else:
        if rek(T, zadana, rown(zastepcza, T[j]), i+1, j+1) or rek(T, zadana, zastepcza+T[j], i+1, j+1) or rek(T, zadana, zastepcza, i, j+1):
            return True
    return False

def rown(a, b):
    return (a*b)/(a+b)

T=[2, 2, 1, 4, 8]

print(rek(T, 14, 0, 0, 0))