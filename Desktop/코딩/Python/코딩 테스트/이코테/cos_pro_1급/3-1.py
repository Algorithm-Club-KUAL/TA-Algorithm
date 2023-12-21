#2배로 늘리는 함수
def func_a(arr):
    ret = arr + arr
    return ret

# c == 0이 아닌게 있으면 아예 다른 수가 있는거여서 같이질 가능성 x
def func_b(first, second):
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True

#부분 리스트 비교
def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False
    if func_b(arrA,arrB):
        arrA_temp = func_a(arrA)
        if func_c(arrA_temp,arrB):
            return True
    return False

arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
print(solution(arrA1, arrB1))

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
print(solution(arrA2, arrB2))