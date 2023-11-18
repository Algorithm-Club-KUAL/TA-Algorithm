from itertools import permutations

n = int(input())

lst = list(map(int,input().split()))
3
dct_lst = list(map(int, input().split()))
dct = {}
dct['+'] = dct_lst[0]
dct['-'] = dct_lst[1]
dct['*'] = dct_lst[2]
dct['//'] = dct_lst[3]

result_lst = []

dct_lst_tempt = [ x for x in ('+' * dct['+']+'-' * dct['-']+'*' * dct['*']+'//' * dct['//']) ] 
dct_calc = permutations(dct_lst_tempt, n-1)

result = lst[0]
for calc in dct_calc: #calc는 ( 연산자들의 순열 중 하나의 경우 )
    expr = 'result'
    for i, operator in enumerate(calc): # operator는 연산자 하나
        expr += f'{operator}'
        expr += f'{lst[i+1]}'
    result = eval(expr)
    result_lst.append(result)
print(max(result_lst))
print(min(result_lst))

#ㅅㅂ 왜이리 안 되는데;;