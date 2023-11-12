def solution(arr):
    #임시 비교 값
    answer = 0 

    #만약 증가하는 수가 나오면 바로 2가 되기 떄문에 1로 초기화
    temp = 1 

    #i번쨰 인덱스 값과 i+1번쨰 인덱스 값 비교
    for i in range(len(arr)-1):
        
        #증가하는 수가 나옴
        if arr[i] < arr[i+1]:
            temp += 1

        #더이상 증가하지 않음
        else:
            #지금까지 하면서 저장된 최대연속경우와 방금 구한 연속경우 비교
            answer = max(temp,answer)
            temp = 1
        
        """
        만약에 arr가 마지막까지 증가하다가 끝나면
        if문에 temp 값만 오르다가 종료되기 떄문에
        그럴 경우를 대비해서 밖에도 max(temp,answer) 코드를 작성함.
        """
    
        answer = max(temp,answer)
        
    return answer

#test
#arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4, 5, 6, 7]
arr = [3,2,1]
print(solution(arr))