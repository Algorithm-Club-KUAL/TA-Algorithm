repeat = int(input())
lst = []
for _ in range(repeat):
    lst.append(int(input()))
lst.sort()
for i in lst:
    print(i)