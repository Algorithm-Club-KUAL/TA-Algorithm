byte = int(input())

repeat = byte // 4

str = 'long'
for _ in range(repeat -1):
    str += ' long'
print(str+' int')