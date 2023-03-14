def rek(T,targetSum,sum=0,y=0,col=[],empty=True):
    print(sum, y, col, empty)
    if y==len(T):
        if targetSum==sum and empty==False:
            return True
        return False
    for x in range(len(T)):
        if x in col:
            continue

        if rek(T,targetSum,sum+T[y][x],y+1,[*col,x],False) or rek(T,targetSum,sum,y+1,col,empty):
            return True
    return False

arr = [
    [1,4,7],
    [12,8,4],
    [123,8,42]
]

print(rek(arr,9))