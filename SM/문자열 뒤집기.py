S = input()
list = []
temp = ''
One = 0
Zero = 0
cnt = 0
for i in range(len(S)):
    str = S[i]
    if str == temp:
        temp = str
    elif str != temp:
        list.append(str)
        temp = str
        
for i in list:
    if i == '1':
        One +=1
    elif i == '0':
        Zero +=1



if One > Zero:
    print(Zero)
elif Zero >= One:
    print(One)
