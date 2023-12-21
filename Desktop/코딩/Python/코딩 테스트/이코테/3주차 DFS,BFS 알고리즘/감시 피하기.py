from itertools import combinations # 조합 모듈

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input().split()))

def dfs(x, y, graph):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    for i in range(n): # 가로(x의 행) 확인
        if graph[x][i] == 'S':  
            return False
        elif graph[x][i] == 'O': #! 벽 만남
            break
    for i in range(n): # 세로(y의 열) 확인
        if graph[i][y] == 'S':  
            return False
        elif graph[i][y] == 'O': #! 벽 만남
            break
    return True

#! 선생님 위치 찾기
location_tuple = [(), ]
for x in range(n):
    for y in range(n):
        if graph[x][y] == 'T':
            location_tuple.append((x, y))

#? 1) 장애물 세우기 위한 모든 경우 만들기
lst_X = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 0:
            lst_X.append(tuple( (x, y) ))
lst = combinations(lst_X, 3) #! 3개씩 묶은 조합 iter
result_lst = []

for wall in lst:
    #? 2) 빈 공간(X)인 경우에 벽(O) 세우기
    graph_tempt = [row[:] for row in graph]  # 깊은 복사로 초기화
    graph_tempt[wall[0][0]] [wall[0][1]] = 'O'
    graph_tempt[wall[1][0]] [wall[1][1]] = 'O'
    graph_tempt[wall[2][0]] [wall[2][1]] = 'O'
    for location_teacher in location_tuple:
        result_lst.append(dfs(location_teacher[0], location_teacher[1], graph_tempt))
print("YES" if True in result_lst else "NO")