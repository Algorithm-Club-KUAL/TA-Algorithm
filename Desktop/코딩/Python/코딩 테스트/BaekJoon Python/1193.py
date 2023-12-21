n = int(input())
line = 1
while True:
    if n <= 0:
        break
    n -= line
    line += 1
line -= 1 # 몇번째 라인인지 확인
n += line -1
#print(f"n의 값: {n}, line의 값:{line}")
if line %2 == 0: #짝수 라인
    deno,nume = 1, line
    for _ in range(n):
        nume -= 1
        deno +=1
if line %2 == 1: #홀수 라인
    deno,nume = line,1
    for _ in range(n):
        deno -=1
        nume +=1
print(f'{str(deno)}/{str(nume)}')
