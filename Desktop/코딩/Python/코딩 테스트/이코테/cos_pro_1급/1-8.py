def solution(N, votes):

    #각 후보가 몇 표를 받았는지 체크
    vote_counter = [0 for i in range(N+1)]
    for i in votes:
        vote_counter[i] += 1
    
    #가장 득표수가 많은 경우가 몇 개인지 체크
    max_val = max(vote_counter)

    answer = []
    #후보를 돌면서 최대 득표수의 투표수를 얻은 후보를 정답 리스트에 추가
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(idx)
    return answer.sort()

N1 = 5
votes1 = [1,5,4,3,2,5,2,5,5,4]
print(solution(N1, votes1))

N2 = 4
votes2 = [1, 3, 2, 3, 2]
print(solution(N2, votes2))