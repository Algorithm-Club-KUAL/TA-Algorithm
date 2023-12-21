n = int(input())
home_lst = list(input().split()) #10 5 2

sort_home = sorted(home_lst) #2 5 10
big = int(sort_home[-1]) #10
distance = []
sum_lst = []

for i in range(1, big+1): #1 ~ 10
    for j in home_lst:  #10 5 2 #안테값이 1일떄의 차를 구하는거
        distance.append(abs(i - int(j)))    #안테나 값을 1 ~ 10을 돌면서 하나씩 다 안테나 값의 위치로 넣어보는거죠
    sum_lst.append(sum(distance))
    
antena = sorted(sum_lst)
min = antena[0]

for idx, i in enumerate(sum_lst):
    if i == min:
        print(i)
        break