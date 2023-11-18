num_lst = []
idx = 0     #idx는 최댓값의 인덱스 0이라고 대충 초기화 한거다.
for _ in range(9):
    num_lst.append(int(input()))

for i in range(9):  #i 0~8
    if num_lst[i] < num_lst[idx]:   #i번인덱스 idx인덱스 비교
        continue
    elif i == idx:
        continue
    else:
        idx = i

#num_lst[idx] 얘가 진짜 최댓값임 ㅇㅇ
for i in range(9):
    
    if num_lst[i] == num_lst[idx]:#최댓값이 하나 더있으면
        print(i+1)

"""
lst = []
for _ in range(9):
    lst.append(int(input()))
    
print(max(lst), end="\n")
print(lst.index(max(lst))+1)
"""