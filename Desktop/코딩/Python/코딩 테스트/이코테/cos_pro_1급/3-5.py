def solution(phrases, second):
    answer = ''
    length = len(phrases)
    answer = '_'*(length-second)
    for i in range(second):
        answer +=  phrases[i]
    return answer

phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")