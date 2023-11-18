lst_x = []
lst_y = []
for i in range(3):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)

if lst_x[0] == lst_x[1]:
    print(lst_x[2], end=" ")
elif lst_x[0] == lst_x[2]:
    print(lst_x[1], end=" ")
elif lst_x[1] == lst_x[2]:
    print(lst_x[0], end=" ")

if lst_y[0] == lst_y[1]:
    print(lst_y[2], end="")
elif lst_y[0] == lst_y[2]:
    print(lst_y[1], end="")
elif lst_y[1] == lst_y[2]:
    print(lst_y[0], end="")
