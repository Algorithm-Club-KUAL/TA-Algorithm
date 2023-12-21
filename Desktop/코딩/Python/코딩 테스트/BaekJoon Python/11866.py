N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []
idx = 0
while lst:
    idx += K - 1
    if idx >= len(lst):
        idx %= len(lst)
    ans.append(str(lst.pop(idx)))
print("<",end="")
for i in range(len(ans)-1):
    print(f"{ans[i]}, ",end="")
print(f"{ans[-1]}>")