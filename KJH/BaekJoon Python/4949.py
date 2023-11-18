while True:
    lst = []
    a = input()
    if a == '.':
        break
    for i in a:

        if i == '(' or i == '[':
            lst.append(i)
        elif i ==')':
            if len(lst) != 0 and lst[-1] == '(':
                lst.pop()
            else:
                lst.append(i)
                break
        elif i ==']':
            if len(lst) != 0 and lst[-1] == '[':
                lst.pop()
            else:
                lst.append(i)
                break
    if len(lst) == 0:
        print('yes')
    else:
        print('no')
