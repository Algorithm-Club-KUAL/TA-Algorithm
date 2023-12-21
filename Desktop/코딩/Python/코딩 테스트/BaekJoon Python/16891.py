n=int(input())**2
ans=0
A=0         #정지
B=-1000000  #오른쪽에서 다가오니깐 대충 엄청 큰 마이너스

while True:
    if 0<=A<=B: #둘 다 오른쪽으로 가게 되면 부딪힐 일이 없어서
        break
    
    ans+=1
    a = (1-n)/(1+n)*A + 2*n/(1+n)*B
    B = 2/(n+1)*A + (n-1)/(n+1)*B  # -가 아닌 이유는 B가 음수여서
    A = a
    if A < 0:   #벽이랑 충돌 
        ans+=1  
        A*=-1   #부호만 변경
print(ans)