def bin_search(arr, x, start, end):
    mid = (start + end) // 2
    if start >= end:
        return None
    elif arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return bin_search(arr,x, start, mid - 1)
    elif arr[mid] < x:
        return bin_search(arr,x,mid+1, end)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

arr.sort() #오름차순

for x in order:
    result = bin_search(arr,x,0,len(arr))
    if result == None:
        print("No", end=' ')
    else:
        print("Yes", end=' ')

