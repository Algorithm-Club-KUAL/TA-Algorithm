def solution(prices):
    INF = 1000000001
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            answer = max(answer, price- tmp)
        tmp = min(tmp, price)
    return answer

prices1 = [1, 2, 3]
print(solution(prices1))

prices2 = [3, 1]
print(solution(prices2))