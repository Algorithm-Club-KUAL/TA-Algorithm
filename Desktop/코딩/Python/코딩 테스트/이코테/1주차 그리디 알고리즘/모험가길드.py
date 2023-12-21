#공포도가 높으면 공포를 쉽게 느낌  x = 1
#공포도가 x면 x명이 있어야댐. 가장 공포도가 높은 얘가 가장 많은 인원을 가지고 있는 길드를 만들텐데
#그떄 나머지 얘들도 최대한으로 공포도가 높은 얘들이여야 그룹 수를 많이 만들 수 있음.
"""
예제 입력
6
2 3 1 2 2 6 -> 1개
1 2 2 2 3 6
1 22 6<- 
"""
n = int(input())
data = list(map(int, input().split()))
data.sort() #오름차순
group = 0
member = 0
for x in data: #1 
    while(True):
        member += 1
        if member == x:
            group += 1
            for _ in range(member):#1
                del data[0]
            member = 0
            break # while문 break
print(group)


