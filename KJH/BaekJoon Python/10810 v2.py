n , m = map(int, input().split())
lst = [0 for x in range(n)]
for i in range(m):
    st,en,num = map(int, input().split())
    for i in range(st-1,en):
        lst[i] = num

for i in lst:
    print(i, end= " ")