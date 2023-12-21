from collections import deque

#deque에 리스트를 넣어준 느낌쓰
# my_list = [1,2,3]
# que = deque([my_list])
# #print(que) #deque([[1, 2, 3]])
# print(que[0])

def bfs (graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                que.append[i]
                visited[i] = True