def szuk(t):
    maxKrok=0
    for y in range(len(t)-1):
        for x in range(len(t)-1):
            yC=y
            xC=x
            iloraz=t[y][x+1]/t[y][x]
            # print(iloraz)
            spr=iloraz
            krok=0
            while spr==iloraz and xC+1<len(t) and yC+1<len(t):
                xC+=1
                # print(t[yC][xC],t[yC][xC-1],"bok",t[yC][xC-1] / t[yC][xC])
                spr =  t[yC][xC]/t[yC][xC-1]
                if spr==iloraz:
                    krok+=1
                    maxKrok=max(maxKrok,krok)
                    yC+=1
                    # print(t[yC-1][xC],t[yC][xC],"dol")
                    spr = t[yC][xC] / t[yC-1][xC]
                    if spr==iloraz:
                        maxKrok = max(maxKrok, krok)
                        krok+=1
    if maxKrok>=3:
        return True,maxKrok
    return False




t=[[1,2,8,9],
    [3,4,8,6],
    [1,2,16,4],
    [2,6,60,8]]
print(szuk(t))
