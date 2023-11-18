n = int(input())
lst = []

for _ in range(n):
    student = input().split()
    lst.append(student)

lst.sort(key=lambda x:(int(-x[1]),int(x[1]), -int(x[2]), x[0]))

for student in lst:
    print(student[0]) 