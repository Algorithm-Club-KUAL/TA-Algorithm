accident = 0
while True:
    n = int(input())
    if n == 0:
        break
    names = [input() for x in range(n)]
    accident += 1
    MyDict = {}
    for i in range(2*n -1 ):
        num, alpha = input().split()
        if num in MyDict:
            del MyDict[num]
        else:
            MyDict[num] = alpha
    answer = int(next(iter(MyDict.keys())))
    print(accident, names[answer-1])