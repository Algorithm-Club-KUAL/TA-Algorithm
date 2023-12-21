# for i in range(4,4):
#     print(i)
# print("실행된거야")

#for i in range(2):
#    print(i)#

#print([ _ for _ in range(1,4)])
# print(0%2)

# arr= [15,15,314,23]
# arr1 = asorted(reverse=True)
# print(type(arr1))

garden = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
n = 3
m = 3
lst = [(x,y) for x in range(n) for y in range(m) if garden[x][y] == 1]
for x,y in lst:
    print(x,y)