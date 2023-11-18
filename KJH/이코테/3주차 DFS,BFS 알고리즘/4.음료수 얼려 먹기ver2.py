N, M = map(int, input("맵 크기: ").split())
frame = []  
for i in range(N):
    frame.append(list(map(int, input(f"{i}행 틀 상황: "))))
dcol = [-1, 0, 1, 0]
drow = [0, 1, 0, -1]

def DFS(col, row):
    if 0 > col or col > N-1 or 0 > row or row > M-1:
        print(f"{row, col}는 범위에 벗어납니다.")
        return False
    
    print(f"-----{row, col}-----")
    for i in range(N): # 디버깅
        print(frame[i])
    
    if frame[col][row] == 0:
        frame[col][row] = 1
    
        print(f"====={row, col}=====")
        for i in range(N): # 디버깅
            print(frame[i])
    
        for i in range(4): # 좌상우하
            DFS(col+dcol[i], row+drow[i])
        print(f"result: {result}")
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if DFS(i, j) == True:
            result += 1 # 결과 값

print(result)