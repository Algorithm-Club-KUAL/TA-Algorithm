lst = []
for _ in range(9):
    lst.append(list(map(int, input().split())))
#table = [list(map(int, input().split())) for _ in range(9)]

max = -1
max_idx = [-1,-1]
for i in range(9):
    for j in range(9):
        if max < lst[i][j]:
            max = lst[i][j]
            max_idx[0] = i
            max_idx[1] = j
print(max)
print(max_idx[0]+1,max_idx[1]+1)