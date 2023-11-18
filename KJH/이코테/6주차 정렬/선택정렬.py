array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j  #뒤에 있는 숫자가 더 크면 인덱스 번호를 바꿈
    array[i],array[min_idx] = array[min_idx], array[i]

print(array)