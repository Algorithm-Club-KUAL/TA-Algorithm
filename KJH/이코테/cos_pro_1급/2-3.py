def func_a(n):
    ret = 1
    while n > 0:
        ret *= 10
        n -= 1
    return ret

#ret:0,1,2,3 
#n:365,36,3,0
#n의 자릿수를 return 
def func_b(n):
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret

#n: 365, 36, 3, 0
#ret: 0, 5, 6, 3 -> 14
#각 자릿수의 합
def func_c(n):
    ret = 0
    while n > 0:
        ret += n%10
        n //= 10
    return ret

def solution(num):
    next_num = num
    while True:
        next_num += 1
        length = func_b(next_num)
        #홀수면 밑에 가지말고 1이나 더해라
        #경품 조건 중에 짝수여야한다 있음.
        if length % 2 == 1: 
            continue
        
        #자릿수 반갈죽
        divisor = func_a(length//2) #생각하기 어려움  
        front = next_num // divisor
        back = next_num % divisor
        
        front_sum = func_c(front)
        back_sum = func_c(back)
        if front_sum == back_sum:
            break
            
    return next_num - num

num1 = 1
print(solution(num1))

num2 = 235386
print(solution(num2))