#map n x m(4,4)
def bfs(x,y):
    print(x,y)
    if x == -1 or y == -1 or x == n or y == m : #지도를 나가면 안되요.
        return 0 #더이상 아무것도 안한다. 
    
    if graph[x][y] == 0:
        #debug
        graph[x][y] = 1 
        bfs(x,y-1)  #상
        bfs(x,y+1)  #하
        bfs(x-1,y)  #좌
        bfs(x+1,y)  #우
        return 1
    return 0
         
#디버기용 
#n,m =4,5 
#graph=[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]


n, m = map(int, input().split())    #4 5
#assginment
graph = []
count = 0

#이중리스트를 만든거 과정
for i in range(n):
    graph.append([])
    j = input() #00110
    for k in j:
        graph[i].append(int(k)) #[[0,0,1,1,0]]
#print(graph)

for i in range(n):
    for j in range(m):
            if bfs(i,j) == 1:
                count += 1
print(count)

