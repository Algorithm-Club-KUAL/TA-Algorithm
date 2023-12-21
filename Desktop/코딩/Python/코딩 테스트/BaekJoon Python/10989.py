#1트
import sys
input = sys.stdin.readline
#input()
#시간을 좀 더 단축해준다. input()보다

repeat = int(input())
lst = []
for _ in range(repeat):
    lst.append(int(input()))
    lst.sort()

for k in lst:
    print(k)


#2트
import sys
repeat = int(sys.stdin.readline())
b = [0] * 10001
#1
#5
#7 b[7] = 1
#  b[1] = 1
#b[1] = 1
#1

for i in range(repeat):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)
            #직접적으로 정렬을 사용한건 아니지만 배열의 값을 늘려주고 순서대로 출력을 해줌으로서 간접적으로 정렬
            #b[7] = 1, b[1] = 1