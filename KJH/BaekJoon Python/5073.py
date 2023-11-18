while True:
    lst = list(map(int,input().split()))
    lst.sort()
    if lst[0] + lst[1] + lst[2] == 0:
        break        
    if lst[0] == lst[1] == lst[2]:
        print("Equilateral")
    elif lst[0] + lst[1] <= lst[2]:
        print("Invalid")
    elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
        print("Isosceles")
    else:
        print("Scalene")