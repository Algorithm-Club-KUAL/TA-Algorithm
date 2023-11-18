def solution(num):
    # Write code here.
    num += 1
    answer = 0
    answer = ''.join('1' if x == '0' else x for x in str(num))
    return answer

#The following is code to output testcase.
num = 9949999
print(solution(num))
