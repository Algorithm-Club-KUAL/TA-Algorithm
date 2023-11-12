def solution(bishops):
    answer = 0
    map = [[0]*9 for _ in range(9)]
    dx = [1,1,-1,-1]
    dy = [1,-1,1,-1]

    for bishop in bishops:
        x = ord(bishop[0]) - ord('A') + 1
        y = int(bishop[1])
        if map[y][x] == 0:
            map[y][x] = 1 #방문체크

        for i in range(len(dx)):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx <= 8 and nx > 0) and (ny <= 8 and ny > 0):
                    x,y = nx,ny
                    if map[y][x] == 0:
                        map[y][x] = 1
                else:
                    x,y = ord(bishop[0]) - ord('A') + 1 , int(bishop[1])
                    break
                
    for i in map:
        print(i)
        for j in i:
            if j == 0:
                answer +=1
    return answer - 9 - 8

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

# #[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")