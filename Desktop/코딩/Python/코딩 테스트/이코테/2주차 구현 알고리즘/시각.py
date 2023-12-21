#첫 줄에는 0시 0분 0초에서 n시 59분 59초까지 셀 때 쓸 n 값의 입력을 받는다.
n = int(input())

whole_sec = n * 3600 + 59 * 60 + 59 #전체 초
sec = 0
min = 0
hour = 0
count = 0
while (hour *3600 + min * 60 + sec < whole_sec):
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
    if min == 60:
        min = 0
        hour += 1
    if "3" in str(sec) + str(min) + str(hour): 
        count += 1
print(count)


