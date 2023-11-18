array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    #pivot 보다 작은 값들의 모임 리스트
    left_pivot = [x for x in tail if x <= pivot] 
    
    #pivot 보다 큰 값들의 모임 리스트
    right_pivot = [x for x in tail if x > pivot]

    return quick_sort(left_pivot) + [pivot] + quick_sort(right_pivot)
print(quick_sort(array))