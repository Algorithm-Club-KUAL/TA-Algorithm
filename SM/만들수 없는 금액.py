N = input()
list1 = list(map(int, input().split()))
target = 1

list1.sort() #동전 오름차순으로 정렬

for i in list1:
    if target >= i :
        target +=i
    elif target < i:
        break
    
print(target)        
             