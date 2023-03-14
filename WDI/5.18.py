import math

tab = [[3, 5, 8], [8, 4, 7], [4, 1, 7]]
# tab=[[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47],[12,37,34,48,23,42,51,47]]
def pierw(l):
    # print(l)
    n=int(math.log10(l))
    new=l//(10**n)
    return new

def print_tab(tab):
    for line in tab:
        print(line)

print_tab(tab)
def rek(tab, x, y):
    print(x, y)
    if x == len(tab)-1 and y == len(tab)-1:
        return True
    ostatnia = tab[x][y] % 10
    if x < len(tab) and y + 1 < len(tab):
        if pierw(tab[x][y + 1]) > ostatnia:
            if rek(tab, x, y + 1):
                return True
    if x + 1 < len(tab) and y < len(tab):
        if pierw(tab[x + 1][y]) > ostatnia:
            if rek(tab, x + 1, y):
                return True
    if x + 1 < len(tab) and y + 1 < len(tab):
        if pierw(tab[x + 1][y + 1]) > ostatnia:
            if rek(tab, x + 1, y + 1):
                return True
    return False

print(rek(tab, 0, 0))
