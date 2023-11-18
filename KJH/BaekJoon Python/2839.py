#3를 5 빼서 최소한으로 뺴끼
#안나눠떨어지면 -1 

n = int(input())
count = 0
while(1):
    #5kg 종량제를 쓰는게 >> 3kg 종량제
    if n % 5 == 0:
        count += int(n/5)
        print(count)
        break
    n -= 3
    count +=1

    if n == 0:
        print(count)
        break
    elif n < 3:
        print(-1)
        break

