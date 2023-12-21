num, idx = map(int,input().split())
lst = []
for i in range(1,num+1):
    if num % i == 0:
        lst.append(i)
try:
    print(lst[idx-1])
except:
    print(0)