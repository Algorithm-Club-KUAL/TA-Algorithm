str_ = input()
size = len(str_)
answer = set()
for i in range(size):
    for j in range(i,size):
        answer.add(str_[i:j+1])
print(len(answer))