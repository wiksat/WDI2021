def chess(T):
    sy = [0] * len(T)
    sx = [0] * len(T)

    for x in range(len(T)):
        for y in range(len(T)):
            sx[x] += T[y][x]
            sy[y] += T[y][x]
    print(sx)
    print(sy)
    best_s = 0
    best_x1 = 0
    best_y1 = 0
    best_x2 = 0
    best_y2 = 0
    for x1 in range(len(T)):
        for y1 in range(len(T)):
            for x2 in range(len(T)):
                for y2 in range(len(T)):
                    if x1 == x2 and y1 == y2:
                        continue
                    if x1 != x2 and y1 != y2:
                        s1 = sx[x1] + sy[y1] - 2 * T[y1][x1]-T[y2][x1]
                        s2 = sx[x2] + sy[y2] - 2 * T[y2][x2]-T[y1][x2]
                    elif x1 == x2 and y1 != y2:
                        s1 = sx[x1] + sy[y1]-2 * T[y1][x1]
                        s2 = sy[y2]- 2 * T[y2][x2]
                    elif y1 == y2 and x1 != x2:
                        s1 = sx[x1] + sy[y1]-2 * T[y1][x1]
                        s2 = sx[x2]- 2 * T[y2][x2]
                    if s1+s2>best_s:
                        best_x1= x1
                        best_y1= y1
                        best_x2 = x2
                        best_y2 = y2
                        best_s=s1+s2
    return  best_y1,best_x1 , best_y2,best_x2, best_s


t = [[4, 0, 2],
    [3, 0, 0],
    [6, 5, 3]]
# t=[[1,2,8,9],
#     [3,4,8,6],
#     [1,2,16,4],
#     [2,6,60,8]]
# t=[[1,1,2,3],
#     [-1,3,-1,4],
#     [4,1,5,4],
#     [5,0,3,6]]
print(chess(t))