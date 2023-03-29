n=int(input("정수 N 입력: "))
number_3=0

for hour in range(0,n+1): #0~n 시
    for min in range(0,60): #0~59분
        for sec in range(0,60): #0~59초
            if '3' in str(hour) + str(min) + str(sec):
                number_3 += 1

print(number_3)