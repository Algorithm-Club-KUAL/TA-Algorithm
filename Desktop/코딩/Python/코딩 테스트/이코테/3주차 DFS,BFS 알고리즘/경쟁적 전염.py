n, k = map(int, input().split())

graph = []
for _ in range(n): #! 지도 생성
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split()) #! s는 시간, x 와 y는 좌표

def dfs(x, y, visited_number):
    if x <= -1 or x >= n or y <= -1 or y >= n: #! 범위 제한
            return  
    #! 바이러스가 K인 경우 : visited_number -> K (K는 자연수)
    if graph[x][y] == visited_number:
        if graph[x-1][y] == 0: 
            graph[x-1][y] = visited_number #! 방문 처리
        if graph[x+1][y] == 0: 
            graph[x+1][y] = visited_number #! 방문 처리
        if graph[x][y-1] == 0: 
            graph[x][y-1] = visited_number #! 방문 처리
        if graph[x][y+1] == 0: 
            graph[x][y+1] = visited_number #! 방문 처리
        
        dfs(x-1, y, visited_number) #상
        dfs(x+1, y, visited_number) #하
        dfs(x, y-1, visited_number) #좌
        dfs(x, y+1, visited_number) #우
        #쭉       상의 상하좌우, 하의 상하좌우, 우의 상하좌우, 좌의 상하좌우
        #쭉
        #쭉
        #상하좌우 계속 바뀜!
        #!주변 상하좌우 바뀐 상태이므로 (visited_number = 1 경우) 끝.
    return
#! 바이러스(k개) 초기 위치 찾기
virus_location_tuple = [ (), ]
for location in range(1, (k)+1):
    for x in range(n): # 행 기준
        for y in range(n): # 열 기준
            if graph[x][y] == location: #! location == 바이러스 1,2,...,k인 경우
                virus_location_tuple.append( tuple( (x, y) ) ) # [ (), (0, 0), (0, 2), (2, 0) ]

for i in range(1, (k)+1):
    dfs(virus_location_tuple[i][0], virus_location_tuple[i][1], i)

print(graph)