n= int(input("n의 크기 입력: "))
move = list(map(str, input().split()))  #U D R L 입력

x=1 
y=1 #첫 시작 좌표 (1,1)

for i in range(len(move)):
    if move[i] == 'U':
        if x==1:
            continue
        else:
            x -= 1

    elif move[i] == 'D':
        if x==n:
            continue
        else:
            x += 1

    elif move[i] == 'L':
        if y == 1:
            continue
        else:
            y -= 1

    elif move[i] == 'R':
        if y == n:
            continue
        else:
            y += 1

print(x,y)