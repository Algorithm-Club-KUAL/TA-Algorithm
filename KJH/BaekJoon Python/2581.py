start = int(input())
end = int(input())
lst = []
for i in range(start, end + 1):
    cnt = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            lst.append(i)
            
if len(lst) <= 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])