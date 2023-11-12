n,m,k = map(int,input().split())
data = [int(i) for i in input().split()]
data.sort(reverse=True)

sum = 0 
cnt = m
while True:

    for _ in range(k):
        if cnt == 0:
            break
        sum += data[0]
        cnt -=1
    if cnt == 0:
        break
    sum += data[1]
    cnt -= 1

print(sum)