def solution(n):
    nlist = [[0]*n for _ in range(n)] #2차원 리스트 선언    
    dir = 0
    dr = [0,1,0,-1] #dir값에 따른 r의 변화량
    dc = [1,0,-1,0] #dir값에 따른 c의 변화량
    r,c = 0 , -1    #r,c 초기 위치 이떄 c가 -1인 이유는 생략
    num = 1
    loop = n

    while num <= n*n:
        for _ in range(loop):
            r += dr[dir]
            c += dc[dir]
            nlist[r][c] = num
            num += 1     
        dir = (dir+1) % 4 
        if dir % 2 == 1:
            loop -= 1
    answer = 0
    for x in range(n):
        answer += nlist[x][x]
    return answer

n1 = 3
print(solution(n1))

n2 = 2
print(solution(n2))