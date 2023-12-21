# from itertools import combinations
# import sys
# input = sys.stdin.readline
# def is_prime(x):
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             return False
#     return True
# n = int(input())
# cnt = 0
# for _ in range(n):
#     num = int(input())
#     lst = []
#     for i in range(2,num):
#         flag = is_prime(i)
#         if flag:
#             if i * 2 == num:
#                 lst.append(i)
#                 lst.append(i)
#             else:
#                 lst.append(i)
#     nCr = list(combinations(lst,2))
#     for i in nCr:
#         if sum(i) == num:
#             cnt += 1
#     print(cnt)
#     cnt = 0
#     lst = []

import sys

t = int(input())

arr = [True for _ in range(1000001)]
for i in range(2,1001):
    if arr[i]:
        for j in range(i + i , 1000001, i):
            arr[j] = False

for _ in range(t):
    result = 0
    n = int(sys.stdin.readline().rstrip())

    for i in range(2,n//2+1):
        if arr[i] and arr[n-i]:
            result += 1
    print(result)