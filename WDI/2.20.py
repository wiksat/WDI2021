def change_base(x,base):
    chars="0123456789abcdef"
    ans=""
    while x!=0:
        ans=chars[x%base]+ans
        x//=base
    return ans
a=11
b=522
flag=True
for x in range(2,16+1):
    if flag:
         a=change_base(a,x)
         aC=a
         b=change_base(b,x)
         bC=b
         while aC>0:
             while bC>0:
                 aC