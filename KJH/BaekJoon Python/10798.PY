lst = [input() for _ in range(5)]
#[[AB],[]]
str = ""
len_row = 0
for i in range(5):
    if len_row < len(lst[i]):
        len_row = len(lst[i])
for j in range(len_row):
    for i in range(5):
        try:
            str += lst[i][j]
        except:
            continue
print(str)
