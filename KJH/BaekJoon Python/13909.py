import sys
import math
input = sys.stdin.readline
n = int(input())
cnt = 0
for num in range(1, n+1):
    if num ** 2 <= n:
        cnt +=1 
print(cnt)