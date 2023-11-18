from bisect import bisect_right,bisect_left

def count_range(a, leftValue, rightValue):
    rightIndex = bisect_right(a,rightValue)
    leftIndex = bisect_left(a,leftValue)
    return rightIndex - leftIndex

a = [1,2,3,3,3,3,4,4,4,9]
a.count(4)

print(count_range(a, 4, 4)) # 4가 몇개농?
print(count_range(a, -1,3)) #-1~3가 몇개농?