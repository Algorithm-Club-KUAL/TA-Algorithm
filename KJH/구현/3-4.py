def solution(s1, s2):
    answer = 0
    s1_len = len(s1)
    s2_len = len(s2)
    for i in range(s1_len):
        if s1[i:] == s2[0:s1_len-1]:
            break
    else:
        pass
    n1 = i 
    for i in range(s2_len):
        if s2[i:] == s1[0:s2_len-i]:
            break
    else:
        pass
    n2 = i
    answer = s1_len + s2_len - max(n1,2)
    return answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")