#arr 안에 s가 있는지 확인
def func_a(arr, s): 
    return s in arr 

#벨린도름인지 확인
def func_b(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

#모든 벨린도름들을 정렬하고 k번쨰 벨린도름 반환
def func_c(palindromes, k):
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]

def solution(s, k):
    palindromes = []
    length = len(s)
    for start_idx in range(length):
        for cnt in range(1, length - start_idx + 1):
            sub_s = s[start_idx : start_idx + cnt]
            if func_b(sub_s) == True:
                if func_a(palindromes, sub_s) == False:
                    palindromes.append(sub_s)

    answer = func_c(palindromes, k)
    return answer

s1 = "abcba"
k1 = 4
print(solution(s1, k1))

s2 = "ccddcc"
k2 = 7
print(solution(s2, k2))