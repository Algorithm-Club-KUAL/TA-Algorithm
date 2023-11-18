for _ in range(3):
    num = int(input())
    lst = []
    for _ in range(num):
        lst.append(int(input()))
    Sum = sum(lst)
    if Sum == 0:
        print("0")
    elif Sum > 0 :
        print("+")
    else:
        print("-")