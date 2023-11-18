n, m = map(int, input().split()) #nxm
x, y, direct = map(int, input().split())
count = 0       #방문한 땅의 숫자 count
land = []
for _ in range(m): #m이 가로 
    land.append(list(map(int, input().split())))

#방문 위치 저장
d = [[0]*m for _ in range(n)] #nxm 지도가 있는데 그 지도의 값이 모두 0인 셈이져
d[x][y] = 1 #현재위치는 방문 처리

#북0 동1 남2 서3
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
    
    if d[nx][ny] == 0 and land[nx][ny] == 0 : #아직 안가보고 육지
        d[nx][ny] = 1                        #가봤음
        x,y = nx, ny
        count += 1
        turn_time = 0
        continue
    else: #가본 장소이거나 바다이거나
        turn_time += 1
        
    if turn_time == 4: #뒤로가게
        nx = x - dx[direct]
        ny = y - dy[direct]
        if land[nx][ny] == 0: #육지인 경우
            x,y = nx,ny       #아무 문제 없은
        else:
            break
        turn_time = 0
print(count)