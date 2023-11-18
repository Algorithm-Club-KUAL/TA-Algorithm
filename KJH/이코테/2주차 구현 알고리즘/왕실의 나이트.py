location = input()  #알파벳 하나 + 숫자 하나 

row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1 #알파벳 -> 아스키 코드 - 63 + 1
#ex) b면 아스키코드에서 b- a = 1, 거기에 초기 위치 1 더해서 2
moves = [(-2, -1),(-2,1), (2,1), (2,-1), (-1,2), (1,2),(-1,-2),(1,-2)]
cases = 0

#나이트가 취할 수 있는 행동을 하나하나 넣어주돼 체스판을 벗어나면 기각하고 벗어나지 않으면 cases +=`1`
for move in moves:     
    nrow = row + move[0]
    ncol = col + move[1]
    if nrow < 1 or ncol < 1 or nrow > 8 or ncol > 8:
        continue
    else:
        cases += 1
print(cases)