count = int(input())

for i in range(1, count+1): #5 1,2,3,4,5
    print(' '*(count-i) + '*'*(i))  #count - i + i = count
    #                               #3, 2
                                    #2, 3
                                    #1, 4
                                    #0, 5