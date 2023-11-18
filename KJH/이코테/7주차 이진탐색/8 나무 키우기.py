N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees) #이분탐색 검색 범위 설정

while(start <= end):
    mid = (start + end) // 2 #초기 절단기 값
    sum = 0     
    for tree in trees:
        cut = tree - mid
        if cut > 0: 
            sum += cut
    if sum >= M:     #절단기 값이 작아져도 되는 상황
        start = mid + 1
    else :             #다 더했는데 나무의 양이 적은 상황
        end = mid - 1
print(mid)