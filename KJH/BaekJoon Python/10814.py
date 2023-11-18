# age = 14
# name = 'kim'
# num_lst = []
# num_lst.append(age,name)

import sys
input = sys.stdin.readline
n = int(input())
num_lst=[]

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    num_lst.append((age,name))
    
#나이가 같을 경우는 정렬을 바꾸지 않는데 애시당초 원래 입력한 순서가 먼저 가입한 순서이기 떄문이다.
num_lst.sort(key = lambda x:x[0]) 

for i in num_lst:
    print(i[0], i[1])