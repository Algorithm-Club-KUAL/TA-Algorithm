def solution(k):
    answer = []
    for i in range(1, k + 1): #1~k
        square_num = i * i    #1 ~ k^2
        divisor = 1             
        while square_num % divisor != square_num: # 정답
            front = square_num // divisor
            back = square_num % divisor
            divisor *= 10
            if back != 0 and front != 0:
                if front + back == i:
                    answer.append(i)
    return answer
k = 500
ret = solution(k)
print("solution 함수의 반환 값은 ", ret, " 입니다.")