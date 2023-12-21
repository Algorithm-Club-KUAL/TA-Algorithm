
def solution(hour, minute):
    answer = ''
    h_degree = hour * 60 //2
    answer = minute - h_degree
    return answer

hour = 3
minute = 0
ret = solution(hour, minute)
print("solution 함수의 반환 값은 ", ret, " 입니다.")