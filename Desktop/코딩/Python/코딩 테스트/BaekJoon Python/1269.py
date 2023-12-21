n , m = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
result = set1 ^ set2
print(len(result))