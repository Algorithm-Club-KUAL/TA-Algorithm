n = int(input())
dict_ = {}
for _ in range(n):
    a,b = map(str, input().split())
    if b == "enter":
        dict_[a] = b
    else:
        del dict_[a]
dict_ = sorted(dict_.keys(), reverse = True)

for i in dict_:
    print(i)