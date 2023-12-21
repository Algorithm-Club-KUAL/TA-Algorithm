def sol(n, stages):
    stages.sort()
    length = len(stages)
    
    lst = []
    fin_lst = []
    for level in range(1,n+1):
        fail_cnt = stages.count(level)

        if fail_cnt == 0:
            fail = 0
        else:
            fail = fail_cnt / length 
        lst.append((level, fail))
        length -= fail_cnt

    lst.sort(key= lambda x: x[1], reverse=True)

    for i in range(n):
        fin_lst.append(lst[i][0])

    return fin_lst        

print(sol(4,[4,4,4,4]))