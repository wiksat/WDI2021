def conTP(x,y):
    return y-x+7
def conTN(x,y):
    return x+y

def hetman(tab,n,x_tab,y_tab,p_tab,n_tab,i=8):
    print(p_tab,n_tab,i)
    if i==0:
        # print(tab)
        for x in tab:
            print(x)
        return True
    for x in range(n):
        for y in range(n):
            if not x_tab[x] and not y_tab[y] and not p_tab[conTP(x,y)] and not n_tab[conTN(x,y)]:
                x_tab[x]=True
                y_tab[y]=True
                p_tab[conTP(x,y)]=True
                n_tab[conTN(x,y)]=True
                tab[y][x]=1
                # print(y,x)
                if hetman(tab,n,x_tab,y_tab,p_tab,n_tab,i-1):
                    return True
                x_tab[x] = False
                y_tab[y] = False
                p_tab[conTP(x, y)] = False
                n_tab[conTN(x, y)] = False
                tab[y][x] = 0
    return False



tab=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
# print(tab)
hetman(tab,8,[False]*8,[False]*8,[False]*16,[False]*16)