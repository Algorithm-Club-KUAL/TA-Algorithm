while True:
    num = int(input())
    lst = []
    if num == -1: 
        break

    for i in range(1, num):
        if num % i == 0: 
            lst.append(i)
    
    MyStr = f'{num} '
    if sum(lst) == num:
        MyStr += '= '
        MyStr += ' + '.join(map(str, lst))
    else:
        MyStr += "is NOT perfect."
    print(MyStr)