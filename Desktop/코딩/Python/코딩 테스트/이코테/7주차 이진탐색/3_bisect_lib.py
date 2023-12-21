from bisect import bisect_left, bisect_right
a = [1,2,4,4,5]
x = 4

#정렬된 순서를 유지하며 배열 a에 x를 삽입할 인덱스(int) 반환
print(bisect_right(a,4)) #4
print(a)
print(bisect_left(a,4))  #2
print(a)
