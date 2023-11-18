n = input()
start = 0
end = len(n) -1
answer = 1
while start < end:
    if n[start] != n[end]:
        answer = 0
        break
    start += 1
    end -= 1
print(answer)