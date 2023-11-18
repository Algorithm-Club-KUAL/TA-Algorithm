def solution(s):
    s += '#'
    answer = ""
    for i in range(len(s)-1):
        if s[i] == '0' and s[i + 1] != '0':
            answer += '0'
        else: #얘가 1일 떄랑 연속으로 0일때
            if s[i] == '1': #추가한 줄 
                answer += '1'
    return answer

s = "101100011100"
print(solution(s))