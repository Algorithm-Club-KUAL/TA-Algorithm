#등차수열을 만들어야 될 것 같다.
#모든 수들의 간격을 구하고 그 간격들의 최대공약수가 공차가 된다.
#공차를 알면 해당 공차에 나무가 없으면 cnt +1같은 걸 해주면 되지 않을까.
def gcd(a,b):
    while b: #b가 0이면 excape
        a = a%b
        a,b = b,a
    return abs(a)
n = int(input())
lst = []
distance = []
for i in range(n):
    lst.append(int(input()))
    if i != 0:
        distance.append(lst[i] - lst[i-1])
max_dis = distance[0]
for i in range(n-2):
    max_gcd = gcd(distance[i+1]-distance[i], max_gcd)
result = ((lst[n-1] - lst[0])//max_gcd -1) - n + 2
print(result)