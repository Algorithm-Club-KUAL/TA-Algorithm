#N, B = input().split()
N = 'ZZZZ'
B = 36
str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
answer = 0
for i,n in enumerate(N):
    answer += (int(B)**i)*(str.index(n))
print(answer)

print(int('ZZZZ',36))
# num = 9
# print(int('111',2))

# print(bin(9)) #2진수 변환 함수
# print(oct(9)) #8진수 변환 함수
# print(hex(9)) #16진수 변환 함수 