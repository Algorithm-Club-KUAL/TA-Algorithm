N = int(input())
list1 = list(map(int, input().split()))

member = 0
maxfear = -1
group = 0
for i in range(N):
    cur = list1[i]
    maxfear = max(maxfear, cur)
    member += 1
    if member == maxfear :
        member = 0
        group += 1
        maxfear = -1

print(group)
    

