#아오 체스시치

def solution(pos):
    answer = 0
    y = int(pos[1])
    x = ord(pos[0]) - ord('A') + 1

    #나이트가 움직일 수 있는 모든 경우의 수(8)
    dx = [1, 1 ,-1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1] 

    for i in range(8):
        nx,ny = 0,0 #선언
        nx += x + dx[i]
        ny += y + dy[i]
        #print(nx,ny)
        if (nx <= 8 and nx > 0) and (ny <= 8 and ny > 0 ):
            answer += 1
    return answer

pos = "A7"
print(solution(pos))
