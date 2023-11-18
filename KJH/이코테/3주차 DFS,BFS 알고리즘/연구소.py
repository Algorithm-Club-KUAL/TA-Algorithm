from itertools import combinations # 조합 모듈
n, m = map(int, input().split())

graph = []

for _ in range(n): # 지도 생성
    graph.append( list( map( int , input().split() ) ) )

def dfs(x, y, graph): # 바이러스(2) 생성
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return None
    if graph[x][y] == 2:
        if x-1 >= 0 and graph[x-1][y] == 0: 
            graph[x-1][y] = 2
            dfs(x-1, y, graph) #상
        if x+1 <= n-1 and graph[x+1][y] == 0: 
            graph[x+1][y] = 2
            dfs(x+1, y, graph) #하
        if y-1 >= 0 and graph[x][y-1] == 0: 
            graph[x][y-1] = 2
            dfs(x, y-1, graph) #좌
        if y+1 <= m-1 and graph[x][y+1] == 0: 
            graph[x][y+1] = 2    
            dfs(x, y+1, graph) #우

        #쭉       상의 상하좌우, 하의 상하좌우, 우의 상하좌우, 좌의 상하좌우
        #쭉
        #쭉
        #상하좌우 계속 바뀜!
        #주변 상하좌우 바뀐 상태이므로 끝.
        return None
    return None
#! 초기 바이러스의 위치 찾기
virus_location_tuple = [ ]
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            virus_location_tuple.append((x, y))

#? 벽 3개 만들기 1) 우선 모든 경우 구하기
all_case_zero = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            all_case_zero.append(tuple( (x, y) ))
all_case = combinations(all_case_zero, 3) #! 3개씩 묶은 조합 iter
all_case_count = [ ] #? 0개수 세기 위한 용도


graph_tempt = graph

#? 1) 우선 모든 경우 구하기 ->
#! 모든 벽의 경우에 따른 바이러스 확산 
for wall in all_case:
    #? 2) 빈 공간(0)인 경우에 벽(1) 세우기
    # graph_tempt = graph
    graph_tempt = [row[:] for row in graph]  # 깊은 복사(?)로 초기화 - gpt 참고 코드
    #TODO -> 아마 // graph_tempt = graph 했는데 오류.
    graph_tempt[wall[0][0]] [wall[0][1]] = 1
    graph_tempt[wall[1][0]] [wall[1][1]] = 1
    graph_tempt[wall[2][0]] [wall[2][1]] = 1
    
    for location in virus_location_tuple:
        dfs(location[0], location[1], graph_tempt) # 모든 바이러스의 위치에서 깊이 우선 탐색 -> 상하좌우 번식

    total = 0
    for count_graph in graph_tempt: 
        total += count_graph.count(0)
    all_case_count.append(total)
    
print(max(all_case_count))