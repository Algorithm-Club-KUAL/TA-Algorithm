from itertools import combinations

n, m = map(int, input().split())

graph = []
lst_count = []

for _ in range(n):  # 지도 생성
    graph.append(list(map(int, input().split())))

lst_zero = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            lst_zero.append((x, y))

lst = combinations(lst_zero, 3)  # 3개씩 묶은 조합 iter


def dfs(x, y, graph):  # 바이러스(2) 생성
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return None
    if graph[x][y] == 2:
        if x-1 >= 0 and graph[x-1][y] == 0:
            graph[x-1][y] = 2
            dfs(x-1, y, graph)  # 상
        if x+1 <= n-1 and graph[x+1][y] == 0:
            graph[x+1][y] = 2
            dfs(x+1, y, graph)  # 하
        if y-1 >= 0 and graph[x][y-1] == 0:
            graph[x][y-1] = 2
            dfs(x, y-1, graph)  # 좌
        if y+1 <= m-1 and graph[x][y+1] == 0:
            graph[x][y+1] = 2
            dfs(x, y+1, graph)  # 우

        return None
    return None


location_tuple = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            location_tuple.append((x, y))

for wall in lst:
    graph_tempt = [row[:] for row in graph]  # 깊은 복사로 초기화
    graph_tempt[wall[0][0]][wall[0][1]] = 1
    graph_tempt[wall[1][0]][wall[1][1]] = 1
    graph_tempt[wall[2][0]][wall[2][1]] = 1

    for location in location_tuple:
        dfs(location[0], location[1], graph_tempt)
        
    lst_count.append(sum(row.count(0) for row in graph_tempt))
    graph_tempt = [row[:] for row in graph]  # 깊은 복사로 초기화

print(max(lst_count))

'''
문제의 해결을 위해 코드를 분석해보면 다음과 같은 문제점이 있습니다:

graph_tempt를 graph로 초기화하는 부분에서 문제가 발생합니다. 
graph_tempt = graph는 graph_tempt가 graph의 참조(reference)를 가지도록 만듭니다. 
즉, graph_tempt를 변경하면 graph도 변경됩니다. 따라서 graph_tempt를 초기화하기 위해 
graph_tempt = [row[:] for row in graph]와 같이 깊은 복사(deep copy)를 사용해야 합니다.

lst_count에는 모든 벽의 경우에 따른 바이러스 확산이 반영되어야 합니다. 
현재 코드에서는 각각의 경우에 대해 lst_count를 구한 뒤에 초기화하지 않고 누적되어 결과가 올바르게 나오지 않습니다. 
따라서 각 경우마다 lst_count를 초기화해야 합니다.

다음은 수정된 코드입니다:

'''
