k=int(input())
step=0.001
x=1
area=0
while x<k:
    area += step * 1/x
    x += step
print(area)