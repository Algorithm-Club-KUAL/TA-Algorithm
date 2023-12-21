def dfs(graph, v, visted):
    visted[v]= True     #방문했다.
    print(v, end=' ')

    for i in graph[v]:  #graph[v]는 v번쨰 노드에 연결된 노드
        if not visted[i]:   #재귀함수
            dfs(graph,i,visted) #i = 2


#이해완료
graph =[
    [],         
    [2,3,8],    #graph[1] -> 1번 노드
    [1,7],      #grapg[2] -> 2번 노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
#디폴트가 false고 방문할 떄마다 True로 바꿔줄거임 ㅇㅇ
visited = [False] * 9

dfs(graph, 1, visited)  #한 노드와 연결된 정보가 담긴 리스트, 첫번쨰로 방문할 리스트의 인덱스번호, 방문 여부 확인 리스트