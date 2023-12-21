#첫 줄에는 n x n에서 n에 해당하는 값이
#그 다음 줄에는 L,R,U,D가 공백으로 나눠져 입력된다. 
n = int(input())
moves = list(input().split())   #R R R U D D

#시작 x,y 위치
x,y = 1, 1

#L,R,U,D에 따른 움직임
actions = ['L','R','U','D'] 
dx =[0,0,-1,1]              
dy = [-1,1,0,0]     

for move in moves:  #R R R U D D
    for i in range(len(actions)):
        if move == actions[i]: #R = =R , 1
            #nx, ny로 받아주는 이유는 범위를 벗어났을떄 무시하기 위해서이다.
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:   #주워진 범위를 벗어나면 안된다
        continue

    x, y = nx, ny
print(x,y) ###정답