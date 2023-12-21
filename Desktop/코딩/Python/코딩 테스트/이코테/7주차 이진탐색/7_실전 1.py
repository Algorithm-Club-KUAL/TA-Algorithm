from bisect import bisect_left, bisect_right

def search_range(arr, leftValue, rightValue):
    leftIndex = bisect_left(arr, leftValue)
    rightIndex = bisect_right(arr, rightValue)
    return rightIndex - leftIndex

n,m = map(int, input().split())
lst = list(map(int, input().split()))

result = search_range(lst, m,m)
if result <= 0:
    print(-1)

else:
    print(result)