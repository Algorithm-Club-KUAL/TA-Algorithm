repeat = int(input())
units = [25, 10, 5, 1]
ans =""
for _ in range(repeat):
    money = int(input())
    for unit in units:
        ans += str(money // unit)
        money %= unit 
        ans += " "
    print(ans)
    ans =""

# n = int(input())

# for _ in range(n):
# 	money = int(input())
# 	for i in [25, 10, 5, 1]:
# 		print(money//i, end=' ')
# 		money = money%i
