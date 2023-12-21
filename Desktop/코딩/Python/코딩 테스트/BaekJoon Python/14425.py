n,m = map(int, input().split())
set_ = set([input() for _ in range(n)])
cnt = 0
for _ in range(m):
    check = input()
    if check in set_:
        cnt += 1
print(cnt)