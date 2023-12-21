MyStr = input()
result = 0
for i in range(len(MyStr)):
    fir = int(MyStr[i])
    if (fir == 0)  or (fir == 1):
        result = result + fir
    elif (result == 0):
        result += fir
    else:
        result = result * fir 
print(result)
