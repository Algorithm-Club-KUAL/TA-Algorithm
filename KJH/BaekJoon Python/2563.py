Map = [[0]*100 for _ in range(100)]
repeat = int(input()) #반복 횟수
#(3,7) -> (13,17)

for _ in range(repeat):
    x,y = map(int, input().split())
    x2 = x + 10
    y2 = y + 10
    for i in range(y-1,y2-1): #
        for j in range(x-1,x2-1): 
            if Map[i][j] == 0:
                Map[i][j] = 1
cnt = 0
for lst in Map:
    cnt += lst.count(1)
print(cnt)