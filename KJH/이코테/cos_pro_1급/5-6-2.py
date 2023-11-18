#이진수 덧셈 연산을 해보자
#10 / 5 0 2 1 1 0 0 1
def convert(n):
    tmp =''
    while n:
        tmp = str(n%5) + tmp
        n //= 5
        print(f"n의 값 : {n}")
    return int(tmp)

str1 = 8
str2 = str(111)
print(convert(str1))