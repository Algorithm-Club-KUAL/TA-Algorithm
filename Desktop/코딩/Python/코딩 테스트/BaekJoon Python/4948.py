n = -1
cnt = 0
def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True

while (n != 0):
    n = int(input())
    for i in range(n+1,2*n+1):
        flag = is_prime(i)
        if flag:
            cnt += 1
    if cnt != 0:
        print(cnt)
    cnt = 0