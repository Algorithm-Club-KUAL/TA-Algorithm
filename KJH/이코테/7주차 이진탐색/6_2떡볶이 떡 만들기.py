n,m = map(int, input().split())
lst = list(map(int, input().split()))
start = 0
end = max(lst)

while(True):
    mid = (start + end) // 2 #초기 절단기 값
    sum = 0     
    for x in lst:
        cut = x - mid
        if cut > 0: 
            sum += cut
    if sum == m:      #원하는 값이 나온 상황
        break
    elif sum > m:     #절단기 값이 작아져도 되는 상황
        start = mid + 1
    else :             #다 더했는데 나무의 양이 적은 상황
        end = mid - 1
print(mid)