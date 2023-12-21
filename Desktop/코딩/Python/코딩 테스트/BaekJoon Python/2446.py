n = int(input())
for i in range(n):
    print(" "*i+"*"*(2*(n-i)-1))
for j in range(1,n):
    print(" "*(n-j-1) + "*"*(2*(j)+1))
