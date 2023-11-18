repeat = int(input())
lstX=[]
lstY=[]
for _ in range(repeat):
    x,y = map(int, input().split())
    lstX.append(x)
    lstY.append(y)
if repeat == 0:
    print(0)
else:
    width = max(lstX) - min(lstX)
    height = max(lstY) - min(lstY)
    print(width * height)