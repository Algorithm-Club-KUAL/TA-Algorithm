lst = list(map(int, input().split()))
lst.sort()
conditon = lst[0] + lst[1]
if conditon <= lst[2]:
    print(conditon + conditon - 1)
else:
    print(conditon + lst[2])