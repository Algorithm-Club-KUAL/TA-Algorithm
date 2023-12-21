# #sol 1
repeat = int(input())
lst = []
for _ in range(repeat):
    a = int(input())
    lst.append(a)

    if a == 0:      # a == '0' 이라고 하면 안됨.
        lst.pop(-1)
        lst.pop(-1)
print(sum(lst))


# #sol 2
repeat = int(input())
lst = []
for i in range(repeat):
    a = int(input())
    if a == 0:
        lst.pop()
    else:
        lst.append(lst)
print(sum(lst))



#sol 3 안되겠다 야
#repeat = int(input())
#lst = []
#[ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 
#for i in range(repeat):
#    lst = [for x in if x != 0 else lst.pop(-1) for x in x]
lst = [n for n in n in input() if n != 0 else lst.pop(-1) for n in n] 
print(lst)
