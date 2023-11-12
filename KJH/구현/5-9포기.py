def solution(number, target):
    dp = [-1]*(2*target + 1)
    for i in range(1,number+1):
        dp[i] = number -i
        dp[i*2] = dp[i] +i
    dp[number+1] = 1
    print(len(dp))
    print(dp)
number1 = 5
target1 = 9
ret1 = solution(number1, target1)
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)
print("solution 함수의 반환 값은", ret2, "입니다.")