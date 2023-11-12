def solution(arr):
    left, right = 0, len(arr) -1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if left % 2 == 0:
            answer[idx] = arr[left]
            print(f'인덱스와 왼쪽 {idx} {arr[left]}')
            left += 1
        else:
            answer[idx] = arr[right]
            print(f'인덱스와 오른쪽 {idx} {arr[right]}')
            right -= 1
            left +=1
        idx += 1
    return answer

arr = [1, 2, 3, 4, 5, 6]
print(solution(arr))
