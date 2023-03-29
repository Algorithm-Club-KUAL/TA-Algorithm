lst_abc=['a','b','c','d','e','f','g','h']

data=input()

y=int(data[1])
print(y)

x=str(data[0])
print(x)    

int_x=0

for i in range(len(lst_abc)):
    if lst_abc[i] == x:
        int_x= i+1

print(int_x)

#L자 움직임 구문 시작 
# 총 8개의 움직임방법 존재 (8x8 사이즈)
