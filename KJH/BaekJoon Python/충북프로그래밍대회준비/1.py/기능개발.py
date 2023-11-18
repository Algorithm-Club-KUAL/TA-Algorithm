"""
입력첫번째줄에는 progesses가 ,로 구분되어서 입력되고 
두번째줄에는 speeds가 ,로 구분되어 구분되어서 입력됩니다.
기능이 배포되는 날마다 몇 개의 배포가 이루어지는지 ,로 구분해 출력됩니다.
이떄 progesses 순서대로 베포가 이뤄지는데 첫번쨰가 완료되었을 때 뒤에 progesses도 완료가 됐으면 같이 배포가 돼
"""

"""
동작은 상하좌우
빨간 구슬은 구멍에 들어가고 파란 구슬은 들어가면 안됨. (동시도)
기울이는 동작을 그만하는 것은 더이상 구슬이 움직이지 않을 때 까지.
"""

progresses = list(map(int, input().split(",")))
speeds = list(map(int,input().split(",")))
time = 1
answer = []
count = 0

while len(progresses)> 0:
    if (progresses[0] + time*speeds[0]) >= 100: 
        progresses.pop(0)
        speeds.pop(0)
        count += 1
        
    else:
        if count > 0:
            answer.append(count)
            count = 0
        time += 1
print(answer)