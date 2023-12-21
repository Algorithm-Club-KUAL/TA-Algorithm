n = int(input())

lst = []
for _ in range(n):
    name, grade = input().split()
    lst.append([name, int(grade)])

arr = sorted(lst, key = lambda x:x[1])

for student in arr:
    print(student[0], end=' ')