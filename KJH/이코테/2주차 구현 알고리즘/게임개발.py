

n, m = map(int, input().split())
x, y, direct = map(int, input().split())
count = 0       #방문한 땅의 숫자 count
land = []
for _ in range(m):
    land.append(list(map(int, input().split())))

#방문 위치 저장
d = [[0]*m for _ in range(n)]
d[x][y] = 1 #현재위치는 방문 처리

#북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3
turn_time = 0


while(1): #게임 시작
    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    if d[nx][ny] == 0 and land[nx][ny] ==0 : #아직 안가보고 육지
        d[nx][ny] = 1                        #가봤음
        x,y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]

        if land[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_time = 0

print(count)