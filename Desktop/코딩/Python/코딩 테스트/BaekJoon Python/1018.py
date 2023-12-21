n,m = map(int, input().split())
board = [str(input()) for _  in range(n)]
result = []

for x in range(n - 7):
    for y in range(m - 7):
        draw1 = 0
        draw2 = 0
        for i in range(x,x+8):
            for j in range(y, y+ 8):
                if (i+j) % 2 == 0:
                    if board[i][j] != "B":
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if board[i][j] != "W":
                        draw1 += 1
                    else:
                        draw2 += 1
        result.append(min(draw1,draw2))
print(min(result))








n,m = map(int, input().split())
board = [str(input()) for _ in range(n)]
result = []

for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'B':
                        draw1 += 1
                    if board[k][l] != 'W':
                        draw2 += 1
                else:
                    if board[k][l] != 'W':
                        draw1 += 1
                    if board[k][l] != 'B':
                        draw2 += 1   
        result.append(draw1)
        result.append(draw2)
print(min(result))