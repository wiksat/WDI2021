ruchy=[(2,1),(1,2),(-2,1),(-1,2),(-2,-1),(2,-1),(1,-2),(-1,-2)]
def skoczek(T,x,y,n, skoki=1):
    # print(x,y,skoki)
    if skoki==n**2:
        print(T)
        return True
    for ruch in ruchy:
        if x+ruch[1]>=0 and x+ruch[1]<n and y+ruch[0]>=0 and y+ruch[0]<n:
            if T[x+ruch[1]][y+ruch[0]]==0:
                T[x + ruch[1]][y + ruch[0]]=skoki
                if skoczek(T,x+ruch[1],y+ruch[0],n,skoki+1):
                    return True
                T[x + ruch[1]][y + ruch[0]] = 0
    # return False
T=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
skoczek(T,0,0,8)
print(T)
for x in T:
    print(x)