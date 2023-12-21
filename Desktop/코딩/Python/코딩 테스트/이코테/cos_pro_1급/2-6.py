# def solution(commands):
#     x,y = 0,0 #초기 위치
#     #상하좌우
#     actions = ["U","D","L","R"]
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     for i in commands:
#         for j in range(len(actions)):
#             if i == actions[j]:
#                 x = x + dx[j]
#                 y = y + dy[j]
#     return [x,y]

# commands = "URDDL"
# print(solution(commands))

def solution(commands):
    x,y = 0,0 #초기 위치
    #상하좌우
    move = dict(zip('LRUD',[[-1,0],[1,0],[0,1],[0,-1]]))
    for c in commands:
        dx, dy = move[c]
        x += dx
        y += dy
    return [x,y]

commands = "URDDL"
print(solution(commands))