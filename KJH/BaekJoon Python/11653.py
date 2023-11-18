n = int(input())
cnt = 2
while(n != 1):
    if n % cnt == 0:
        print(cnt)
        n /= cnt
        cnt = 2
    else:
        cnt += 1
if cnt == n:
    print(n)