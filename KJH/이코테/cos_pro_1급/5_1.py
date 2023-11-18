def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)]
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] =  sum(steps[1:i])
	answer = steps[n]
	return answer
n1 = 3
ret1 = solution(n1)
print("solution 함수의 반환 값은", ret1, "입니다.")
n2 = 4
ret2 = solution(n2)
print("solution 함수의 반환 값은", ret2, "입니다.")