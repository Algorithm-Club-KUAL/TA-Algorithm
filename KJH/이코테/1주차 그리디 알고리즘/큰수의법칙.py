# 첫 줄: 배열의 갯수, 몇개를 더하는 지, 한번에 몇번까지 더할 수 있는지
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# 디버깅용
# print(data)
# First = data[0] #가장 큰 값
# Second = data[1] #두번쨰로 큰 값

# count = 0
# result = 0
# while(count < m):
#     count += 1
#     for _ in range(k):
#         result += First
#         count+=1
#     result += Second
# print(result)


# 동빈이의 큰수 법칙 -> 주어진 배열이 있을 때 각 수를 M번 더해 가장 큰 수를 만든다.
# 단 각 수가 K번 초과하여 더해지면 안된다.
# 각 수가 같아도 인덱스가 다르면 다른 것으로 취급

N,M,K=tuple(map(int,input().split()))
nums=list(map(int,input().split()))
nums.sort(reverse=True)
ans=0

for i in range(1,M+1):
    if i%K==0:
        ans+=nums[1]

    else:
        ans+=nums[0]
print(ans)