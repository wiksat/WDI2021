tab=[[1,2,3,4,2,4,5,4],[7,3,6,4,5,2,3,6],[3,5,2,6,1,4,6,5],[6,5,4,3,2,1,2,4],[4,3,2,1,6,7,4,5],[8,4,3,2,3,4,6,1],[5,3,4,5,6,4,5,6],[5,3,2,3,5,6,7,4]]

def print_tab(tab):
    for line in tab:
        print(line)
print_tab(tab)
maxi=99999
def koszt(tab,x,ruchy,y,sum):
    global maxi
    # print(tab[y][x])
    sum+=tab[y][x]
    if  y+1<=7:
        if x-1>=0 and ruchy-1>=0:
            koszt(tab,x-1,ruchy-1,y+1,sum)
    else:
        if maxi>sum:maxi=sum
    if y+1<=7:
        if ruchy-1>=0:
            koszt(tab,x,ruchy-1,y+1,sum)
    else:
        if maxi>sum:maxi=sum
    if y+1<=7:
        if x + 1 <= 7 and ruchy - 1 >= 0:
            koszt(tab,x+1,ruchy-1,y+1,sum)
    else:
        if maxi>sum:maxi=sum

koszt(tab,3,7,0,0)
print(maxi)