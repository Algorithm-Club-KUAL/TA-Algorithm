import sys
from collections import deque
n = int(input())
input = sys.stdin.readline
que = deque([])
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        que.append(order[1])
    elif order[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0) 
    elif order[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif order[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])