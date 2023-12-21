s = input().upper() #문장을 입력받음
lst = []            #글자 수 체크
s_set = list(set(s))#문장에 알파벳만 추출

for k in s_set:
    lst.append(s.count(k))#알파벳 개수를 lst에 추가를 하고
if lst.count(max(lst)) > 1:
    print("?")
else:
    print(s_set[(lst.index(max(lst)))])          #가장 많이 사용된 알파벳을 출력