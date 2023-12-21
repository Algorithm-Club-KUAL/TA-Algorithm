#1 2 3 4 5
#3 1 4 2 5
n, m = map(int, input().split())
lst = [x for x in range(1,n+1)]
for i in range(m):
    fir, sec = map(int, input().split())
    lst[fir-1], lst[sec-1] = lst[sec-1], lst[fir-1]
for i in lst:
    print(i, end= " ")