#첫 줄 입력: 행(row) x 열(column)
#두번쨰 줄 이후 입력: 카드들


row,col = list(map(int, input().split()))   
lst=[]

for _ in range(row):
    SecLst = list(map(int, input().split()))
    lst.append(SecLst)
#print(lst) 디버깅용

min_lst = []
for i in lst:   #i는 행
    min = 10001
    for j in i:
        if j < min:
            min = j
    min_lst.append(min)

max = 0
for i in min_lst:
    if i > max:
        max = i
print(max)
