from itertools import combinations

n,m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] ==1:
            house.append((r,c)) #일반집
        elif data[c] == 2:
            chicken.append((r,c))#치킨집

combination = list(combinations(chicken,m))

def get_sum(combnation):
    result = 0
    for hx,hy in house:
        temp = 1e9 #10000000000
        for cx,cy in combination:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result
result = 1e9
for com in combination:
    result = min(result, get_sum(com))

print(result)