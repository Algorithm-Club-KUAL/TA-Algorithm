#4 1
#3 3
#2 5
#1 7
#0 9 

#1 7  
#2 5
#3 3
#4 1
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i -1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+"*"*(2*j -1))