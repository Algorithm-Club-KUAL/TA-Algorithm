n, m = map(int, input().split())
lst = list(map(int, input().split()))
cutter = 0
#cutter의 값이 너무 높으면 m이 안되고 너무 작으면 최댓값이 아님
#초기 cutter의 갑을 어떻게 설정해야하나?
#lst의 중간 값으로 하면 되지 않을까? 일단 bin def를 먼저 만들자
def bin_search(arr,target, start, end):
    if start >= end:
        return None 
    mid = (start + end) // 2
    sum = 0
    for x in arr:
        cut = x - mid
        if x > 0:
            sum += cut
    if sum == target:
        return mid
    elif arr[mid] > target:
        return bin_search(arr,target, start , mid - 1)
    elif arr[mid] < target:
        return bin_search(arr,target, mid + 1, end)

bin_search(lst,m,0,n-1) #이거는 lst에 m이 있느냐를 묻는게 아니여서 def 변형이 필요함,


    