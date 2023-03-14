
# # GLOBALNIE
# T=[1,7,3,5,11,2]
# mini=9999
# wart=0
# def przejscie(T,valSum,indSum,pozycja,ilosc):
#     global mini,wart
#     if valSum == indSum and valSum > 0 and indSum > 0:
#         if ilosc<=mini:
#             mini=ilosc
#             wart=valSum
#     if pozycja<len(T):
#         return przejscie(T,valSum+T[pozycja],indSum+pozycja,pozycja+1,ilosc+1) or przejscie(T,valSum,indSum,pozycja+1,ilosc)
#
#
# przejscie(T,0,0,0,0)
# print(wart)

T=[1,7,3,5,11,2]
def licz(T,valSum=0,indSum=0,i=0,ile=0):
    print(valSum,indSum,i,ile)
    if valSum == indSum and ile != 0:
        return valSum, ile
    if i==len(T):
        return False, 88888
    tmp1=licz(T,valSum+T[i],indSum+i,i+1,ile+1)
    tmp2=licz(T,valSum,indSum,i+1,ile)
    if tmp1[1]<tmp2[1]:
        return tmp1
    else:
        return tmp2
print(licz(T)[0])