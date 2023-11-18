n,k = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort() #오름차순
arrB.sort(reverse=True) #내림차순

for i in range(k):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]

print(sum(arrA))