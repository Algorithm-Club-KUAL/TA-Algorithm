count = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_sceres = []
for i in scores:
    new_sceres.append(i/max_score*100)
print(sum(new_sceres)/count)