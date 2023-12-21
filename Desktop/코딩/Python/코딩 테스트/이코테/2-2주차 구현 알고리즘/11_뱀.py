n = int(input())
k = int(input())

#지도 그림
data = [[0]*(n+1) for _ in range(n+1)]

#방향정보
info = []

#사과 정보 업데이트
for _ in range(k):
    a,b = map(int, input().split())
    data[a][b] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, C):
    if C =="L":
        direction = (direction - 1 ) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simlate():
    x,y = 1, 1 #뱀의 머리 위치
    data[x][y] = 2 #뱀이 존재하는 위치의 값은 2로 함
    direction = 0  #처음에는 동쪽을 보고 있음
    time = 0
    index = 0      #다음 회전 정보
    q = [(x,y)]    #뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y +dy[direction]
        
        #다음 행선지가 맵 범위 안에 있고 또 뱀의 몸통이 없는 자리인지 확인
        if 1 <= nx and nx <= n and ny <= n and data[nx][ny] != 2:
            #그다음에 사과가 있는지 확인
            if data[nx][ny] == 0: #사과가 없음
                data[nx][ny] = 2  #뱀이 왔으니깐 2로 바꿔줌
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0 #꼬리 짜르기 <- 이거 중요
            
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
                #사과가 있는 경우는 꼬리를 짜르지 않는다.
        else: #맵 범위 밖 or 몸통이 존재하는 자리인 경우
            time +=1
            break
        time +=1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index +=1 
        return time
print(simlate())