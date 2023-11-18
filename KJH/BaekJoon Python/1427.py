str_ = str(input())
lst = []
for i in str_:
    lst.append(int(i))
lst.sort(reverse=True)
for j in lst:
    print(j, end="")