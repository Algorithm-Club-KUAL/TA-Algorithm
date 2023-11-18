import sys
input = sys.stdin.readline
lst =[True for _ in range(1000001)]
for i in range(2,1001):
    if lst[i]:
        for j in range(i+i,1000001, i):
            lst[j] = False
t = int(input())
for _ in range(t):
    ans = 0
    num = int(input())
    for i in range(num//2 + 1):
        if lst[i] and lst[num-i]:
            ans +=1
    print(ans)


# lst = [True for _ in range( 1000001)]
# for i in range(2,1001):
#     if lst[i]:
#         for j in range(i+i,1000001,i):
#             lst[j] = False
# t = int(input())

# for  _ in range(t):
#     ans = 0
#     n = int(input())
#     for i in range(2, n//2+1): #반갈죽
#         if lst[i] and lst[n-i]:
#             ans +=1
#     print(ans)