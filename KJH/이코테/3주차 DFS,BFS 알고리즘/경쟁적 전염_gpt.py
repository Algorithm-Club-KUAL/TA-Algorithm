n, k = map(int, input().split())

graph = []
for _ in range(n): # 지도 생성
    graph.append(list(map(int, input().split())))

s, x_, y_ = map(int, input().split()) # s는 시간, x 와 y는 좌표

def dfs(x, y, visited_number): #! ####################################이 함수는 gpt로 손 봄..ㅠ
    if x < 0 or x >= n or y < 0 or y >= n: # 범위 체크 수정
        return

    if graph[x][y] == visited_number:
        if x-1 >= 0 and graph[x-1][y] == 0: 
            graph[x-1][y] = visited_number
        if x+1 < n and graph[x+1][y] == 0: 
            graph[x+1][y] = visited_number
        if y-1 >= 0 and graph[x][y-1] == 0: 
            graph[x][y-1] = visited_number
        if y+1 < n and graph[x][y+1] == 0: 
            graph[x][y+1] = visited_number

virus_location_tuple = [(), ]
for location in range(1, k+1):
    for x in range(n):
        for y in range(n):
            if graph[x][y] == location:
                virus_location_tuple.append((x, y))
# 1초 시점 지남
for i in range(1, k+1):
    dfs(virus_location_tuple[i][0], virus_location_tuple[i][1], i)
# 2초 시점 지남 // 일반화 : T초 시점 지남 (T >= 2)
for _ in range(s-1): # 총 S초 동안 시행되어야 한데 1초 실행되었으니, S-1초 즉 S-1번 시행되면 됨.
    for i in range(1, k+1):
        dfs(virus_location_tuple[i][0]-1, virus_location_tuple[i][1], i)
        dfs(virus_location_tuple[i][0]+1, virus_location_tuple[i][1], i)
        dfs(virus_location_tuple[i][0], virus_location_tuple[i][1]-1, i)
        dfs(virus_location_tuple[i][0], virus_location_tuple[i][1]+1, i)



print(graph[x_-1][y_ -1])
