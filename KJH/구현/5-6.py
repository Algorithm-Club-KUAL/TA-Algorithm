def solution(s1, s2, p, q):
    #s1 to 10진수
    sum_s1 = 0
    for idx,i in enumerate(s1):
        sum_s1 += int(i) * (p **(len(s1)-idx -1))
    print(f"s1 10진수 변환: {sum_s1}")

    #s2 to 10진수
    sum_s2 = 0
    for idx,i in enumerate(s2):
        sum_s2 += int(i) * (p **(len(s2)-idx -1))
    print(f"s2 10진수 변환: {sum_s2}")

    #s1 10진수 to q 진수
    s1_toQ =''
    while sum_s1:
        s1_toQ += str(sum_s1%q)
        sum_s1 //= q
    print(f"s1을 q 진수 변환: {s1_toQ[::-1]}")

    #s2 10진수 to q 진수
    s2_toQ =''
    while sum_s2:
        s2_toQ += str(sum_s2%q)
        sum_s2 //= q
    print(f"s2을 q 진수 변환: {s2_toQ[::-1]}")
    answer = ""
    FinalS1 = s1_toQ[::-1]
    finalS2 = s2_toQ[::-1]
    dec1 = int(FinalS1,8)
    dec2 = int(finalS2,8)
    answer = oct(dec1 + dec2)[2:]
    return answer

s1 = "112001"
s2 = "12010"#138
p = 3 
q = 8 
ret = solution(s1, s2, p, q)
print("solution 함수의 반환 값은", ret, "입니다.")