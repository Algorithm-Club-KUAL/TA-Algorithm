def func_a(times):
    #모든 시간을 분으로 변환
    hour = int(times[:2])
    minute = int(times[3:])
    return hour*60 + minute

def solution(subway_times, current_time):
    #현재 시간 분으로 변환
    current_minute = func_a(current_time)
    INF = 1000000000
    answer = INF
    for s in subway_times:
        #지하철 시간 분으로 변환
        subway_minute = func_a(s)
        
        #현재 시간보다 이후에 있는 지하철 시간
        if subway_minute >= current_minute:
            temp = subway_minute - current_minute

            #현재 시간 이후에 있는 지하철이 한두개가 아닐 거 아니야
            #그중에 가장 작은게 가장 먼저 오는 거겠죵?
            answer = min(temp,answer)

    #오늘 지하철 몽땅 놓침
    if answer == INF:
        return -1
    
    return answer

#test
subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
print(solution(subway_times1, current_time1))

subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
print(solution(subway_times2, current_time2))