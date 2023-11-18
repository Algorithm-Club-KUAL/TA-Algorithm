def func_a(a, b): #더 큰 값 찾기
	mod = a % b
	while mod > 0:
		a = b   #24 9
		b = mod #6
		mod = a % b #3
	return b

def func_b(n):
	answer = 0
	for i in range(1, n+1):
		if func_c(n,i):
			answer += 1
	return answer

def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
    answer = 0
    gcd = func_a(func_a(a,b),c)
    answer = func_b(gcd)
    return answer
a = 24
b = 9
c = 15
ret = solution(a, b, c)
print("solution 함수의 반환 값은", ret, "입니다.")