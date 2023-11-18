# 1 2 3 4 5
# 3 4 1 2 5

n,m = map(int, input().split())
lst = [x for x in range(1,n+1)]

for _ in range(m):
    start , end = map(int, input().split())
    while start <= end:
        lst[start-1], lst[end-1] = lst[end-1] ,lst[start-1]
        start += 1
        end -= 1
        
for i in lst:
    print(i, end= " ")