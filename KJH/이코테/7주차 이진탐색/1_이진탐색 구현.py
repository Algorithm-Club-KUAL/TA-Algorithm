def binary_search(arr, target, start ,end):
    if start > end: #이상한 상황 
        return None
    mid = (start + end) // 2 #정수 나누기
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)

lst = [0,2,4,6,8,10,12,14,16,18]
print(binary_search(lst, 4, 0, 9) +1 ) #인덱스 번호 
