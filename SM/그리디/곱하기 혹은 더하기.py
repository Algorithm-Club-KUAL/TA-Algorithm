S = input()
answer = 0
for i in range(len(S)):
    str = S[i]
    if answer == 0 or answer == 1:
        answer += int(str)
    else:
        answer *= int(str)
print(answer)