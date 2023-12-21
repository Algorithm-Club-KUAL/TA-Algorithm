# import sys
# input = sys.stdin.readline

# repeat = int(input())
# lst = list(map(int, input().split()))
# lst2 = sorted(list(set(lst)))

# for i in lst:
#     print(lst2.index(i), end = " ")

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
#print(dic)
for i in arr:
    print(dic[i], end = ' ')