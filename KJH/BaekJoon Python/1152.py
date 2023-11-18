data= input()
ls= list(data)
count = 1
if data == " ":
    print("0")
else:
    if ls[0]==' ':
        del ls[0]   #원소를 지우는 것 
    if ls[-1]==' ': #마지막 인덱스: -1 
        del ls[-1]
    for i in ls:
        if i==' ': 
            count+=1
    print(count)