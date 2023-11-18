#greed algorithm
money = 1260
count = 0
coin_types = [500, 100, 50, 10] #입력 <- sort()
for coin in coin_types:
    n, money = divmod(money, coin) #return 값이 몫 나머지
    count += n
    #print(n , money)    #디버깅용
    
print(count)