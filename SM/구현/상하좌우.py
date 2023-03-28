N = int(input())

List1 = list(map(str, input().split()))
dx = 1
dy = 1

for i in List1:
    if i == 'R':
        dx +=1
    if i == 'L' and dx > 1:
        dx -=1
    if i == 'D' and dy < N:
        dy +=1
    if i == 'U' and dy > 1:
        dy -=1

print(dy, dx)