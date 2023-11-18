n = int(input())
lst1 = sorted(list(map(int,input().split())))
m = int(input())
lst2 = list(map(int, input().split()))

cnt = {}
for i in lst1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

        
def binarySearch(lst, target, start, end):
    if start > end: #일치하는게 없음
        return 0
    mid = (start + end) // 2
    if lst[mid] == target:
        return cnt.get(target)
    elif lst[mid] > target:
        return binarySearch(lst, target, start, mid -1)
    elif lst[mid] < target:
        return binarySearch(lst, target, mid +1, end)
    
for i in lst2:
    print(binarySearch(lst1, i, 0, len(lst1)-1), end = ' ')
