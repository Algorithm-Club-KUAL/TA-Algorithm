n = int(input())
shape = [500,100,50,10]
cnt = 0
for i in shape:
    cnt += n // i
    n = n % i
print(cnt) 