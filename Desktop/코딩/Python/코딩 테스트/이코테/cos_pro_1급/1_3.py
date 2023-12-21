#두 숫자와 연산자를 받아서 계산 값을 반환
def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB

#몇번쨰 인덱스에 연산자가 있는지 확인
def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index
        
#연산자 인덱스를 기준으로 숫자를 나눔
def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB

def solution(expression):
    #연산자 인덱스 확인
    exp_index = func_b(expression)
    
    #주워진 문자열에 있는 두 숫자 그룹 나누기
    first_num, second_num = func_c(expression, exp_index)
    
    #연산한 결과값 반환
    result = func_a(first_num,second_num,expression[exp_index])
    return result

#test
expression = "123+12"
print(solution(expression))