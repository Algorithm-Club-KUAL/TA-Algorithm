n,m = map(int, input().split())

result = 0
for _ in range(n):
    data = [int(i) for i in input().split()]
    data_min = min(data)    
    result = max(data_min,result)

print(result)