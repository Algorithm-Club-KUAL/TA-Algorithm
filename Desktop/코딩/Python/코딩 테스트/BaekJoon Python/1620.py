n,m = map(int, input().split())
myDict = {}
for i in range(1,n+1):
    a = input()
    myDict[i] = a
    myDict[a] = i
for _ in range(m):
    temp = input()
    if temp.isnumeric():
        print(myDict[int(temp)])
    else:
        print(myDict[temp])
