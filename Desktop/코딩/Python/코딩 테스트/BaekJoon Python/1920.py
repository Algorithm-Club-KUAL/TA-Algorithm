import sys
input = sys.stdin.readline

N = int(input())
An = set(map(int,input().split()))  #set: 함수 (1,1,2) > (1,2)

M = int(input())
Target = list(map(int,input().split()))

for i in Target:
    if i in An:
        print('1')
    else:
        print('0')
#print('1') if i in An else print('0')