import sys
input = sys.stdin.readline
repeat = int(input())
count = 0
lst = []
while (count < repeat):
    count += 1
    lst.append(list(map(int,input().split())))
#디버깅용
#print(lst)

lst.sort(key=lambda item: (item[1], item[0]))

for i in range(repeat):
    print(lst[i][0], lst[i][1])
    