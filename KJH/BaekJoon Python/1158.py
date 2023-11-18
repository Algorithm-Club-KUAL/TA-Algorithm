n, k = map(int,input().split())
idx = 0
lst = []
ans = []
for i in range(1, n+1):
    lst.append(i)
while lst:
    idx += k - 1 
    idx %= len(lst)
    ans.append(lst[idx])
    del lst[idx]
print('<',end="")
for i in range(len(ans)-1):
    print(ans[i], end=", ")
print(ans[-1],end=">")