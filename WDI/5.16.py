def get_Ascii(wyr):
    res=0
    for x in wyr:
        res+=ord(x)
    return res

def getSamo(wyr):
    samo=["a","e","i","o","u"]
    count=0
    for x in wyr:
        if x in samo:
            count+=1
    return count

def wyraz(s1,s2):
    samo=getSamo(s1)
    asci=get_Ascii(s1)
    return rek(s2,samo,asci)

def rek(s2,samo,asci,znaleziony="",i=0):
    # print(znaleziony)
    if samo==getSamo(znaleziony) and asci==get_Ascii(znaleziony):
        return znaleziony
    if len(s2)==i:
        return False
    return rek(s2,samo,asci,znaleziony+s2[i],i+1) or rek(s2,samo,asci,znaleziony,i+1)

print(wyraz("ula","exegg"))