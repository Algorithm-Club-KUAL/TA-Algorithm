def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
T = int(input())
for _ in range(T):
    r, n = map(int, input().split())
    bridge = factorial(n) // (factorial(r) * factorial(n - r))
    print(bridge)