def binary_search(arr, target, start , end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return None
lst = [0,2,4,6,8,10,12,14,16,18]
print(binary_search(lst, 4, 0, 9))

