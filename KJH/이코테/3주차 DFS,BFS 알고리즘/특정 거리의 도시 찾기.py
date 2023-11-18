from collections import deque

def bfs(graph, start ,visited):
    queue = deque([start])  
    dict_count = {start: 0} # ex) x ==1, 1(key)노드의 최단 거리는 0(value)
    visited[start] = True

    while queue: # 큐에는 시작 노드 1이 들어있음.
        v = queue.popleft()
        # print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]: # visited의 인덱스가 곧 노드이고, 해당 요소가 True면 방문했음
                # -> 방문 안 했을 시 if문 실행
                dict_count[i] = dict_count[v] + 1
                queue.append(i) # 큐에 넣어주고
                visited[i] = True #방문 처리
    if k not in dict_count.values():
        print(-1)
        return     
    for (key, value) in dict_count.items():
        if value == k: # 최단 거리(value)가 k인 경우
            print(key)    

# graph는 입력 받기
n, m, k, x = map(int, input().split())
graph = [ [] for _ in range((n+1)+1)] # n+1개의 빈 리스트 생성 : 인덱스 맞추기용 => 1노드-1인덱스, 2노드-2인덱스
for _ in range(m):
    home, away = map(int, input().split()) # 1 2라면 1번 노드에 2노드 경로 추가
    graph[home].append(away)
# graph = [
#     [], #인덱스와 노드 번호 맞춰주기
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]

visited = [False] * len(graph) # 방문 리스트 만들기

bfs(graph, x, visited) # x : 시작노드