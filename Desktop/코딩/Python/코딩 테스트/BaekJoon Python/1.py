column, row = map(int, input().split())

moves = [(1,0),(0,-1)]

result = 0
for move in moves:
    next_r = row + move[0]
    next_c = column + move[1]

    if next_r >= 1 and next_c <= 8 and next_c >= 1 and next_c <= 8:
        result += 1
print(result)