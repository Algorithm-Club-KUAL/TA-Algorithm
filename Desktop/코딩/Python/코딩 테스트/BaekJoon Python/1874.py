"""
첫 숫자가 1이면 바로 종료조건이 성립함.
NO가 나오는 경우에 대한 처리를 아직 못함.
"""
n = int(input())
stack = []
ele = 1
flag = True
ans = []
while True:
    target = int(input())
    if flag: #초기 조건
        stack.append(ele)
        while stack[-1] != target:
            ele += 1
            stack.append(ele)
            #ans.append('+')
            print('+')
        flag = False
        stack.pop()
        print('-')
        #ans.append('-')
        print("STACK 상태: ", stack)
    else:
        if len(stack) == 0 and flag != True:
            break
        while stack[-1] != target:
            if stack[-1] < target:
                stack.append(ele)
                ele += 1
                #ans.append('+')
                print('+')
            else:
                stack.pop()
                print('-')
        stack.pop()
        print('-')
        ele += 1
        #ans.append('-')
        print("STACK 상태: ", stack)

print(ans)