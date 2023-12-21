n = int(input())
for _ in range(n):
    lst = []
    words = str(input())
    for word in words:
        #print(f"word: {word}")
        if word == '(':
            lst.append(word)
        elif word == ')' and len(lst) != 0 and lst[-1] != ')':
            lst.pop()
        else:
            lst.append(word)
        #print(f"lst = {lst}")
    if len(lst) == 0:
        print("YES")
    else:
        print("NO")