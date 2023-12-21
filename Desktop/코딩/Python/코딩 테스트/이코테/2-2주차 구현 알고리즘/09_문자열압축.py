def sol(s):
    ans = len(s)
    for step in range(1, len(s)//+1):
        sentance = ""
        prev = s[0:step]
        cnt = 1

        for j in range(step , len(s), step):
            if prev == s[j:j+step]:
                cnt +=1
            
            else:
                sentance += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step]
                cnt = 1 #reset
        sentance += str(cnt) + prev if cnt >= 2 else prev

        ans = min(ans, len(sentance))
    return ans