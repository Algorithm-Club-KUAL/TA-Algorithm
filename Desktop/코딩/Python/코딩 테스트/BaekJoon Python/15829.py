
repeat = int(input())
string = input()
answer = 0
#abcde
#a 97 - 96
for i in range(repeat): #i: 0 ~ repeat -1
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer)
# % 1234567891)