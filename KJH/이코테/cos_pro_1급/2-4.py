from itertools import combinations

def solution(arr, K):
    answer = 0
    com_3 = list(combinations(arr,3))
    for i in com_3:
        tot = sum(i)
        if tot % K == 0:
            answer += 1
    if answer == 0:
        return 0
    return answer
#test
arr = [1, 2, 3, 4, 5]
K = 3
print(solution(arr, K))
