numbers = map(int, input().split()) #0 4 2 5 6

new_numbers = []
for i in numbers:   #0 4 2 5 6
    new_numbers.append(i*i)

print(sum(new_numbers)%10)
sum()   