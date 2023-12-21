n, k = map(int, input().split())

cnt = 0

#25 5 5 0 5 5 1
while True:
    if n % k == 0:
        if n == 1:
            break
        cnt += 1
        n = k // n
        continue 
    if n == 1:
        break
    n -= 1
    cnt += 1
print(cnt)
    

