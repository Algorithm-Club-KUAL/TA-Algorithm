n = int(input())
lst = []
answer = 0
for _ in range(n):
    lst.append(int(input()))

temp = lst[0]
for i in range(1,len(lst)):
    temp = temp + lst[i]
    answer += temp
print(answer)
