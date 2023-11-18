n = int(input())
lst = []
houses = list(map(int, input().split()))
lst.append(houses)

sum_lst = []
for i in range(n):
    sum = 0
    pivot = lst[0][i]
    #print(f"피벗 값: {pivot}")
    for j in range(n):
        sum += abs(lst[0][j] - pivot)
        #print(f"집 주소 값: {lst[0][j]}")
    #print(sum)
    sum_lst.append((pivot,sum))

sum_lst.sort(key=lambda x:x[1])
print(sum_lst[0][0])    