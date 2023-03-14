def print_tab(tab):
    for line in tab:
        print(line)

def skok(x,y):
    if x<N and y<N and T[y][x]==0 and x>=0 and y>=0:
        T[y][x]=1
        print_tab(T)
        skok(x-2, y-1)
        skok(x-1, y-2)
        skok(x+1, y-2)
        skok(x+2, y-1)
        skok(x-2, y+1)
        skok(x-1, y+2)
        skok(x+1, y+2)
        skok(x+2, y+1)

N=10
T=[[0for i in range(N)]for i in range(N)]
skok(5,5)
print_tab(T)
