# import sys
# while True:
#     for i in range(100):
#         for j in range(100):
#             print(i,j)
#             sys.exit()
# lst = []
# while lst:
#     print(2)
# import sys

# input = sys.stdin.readline
# n = int(input())
# wait = list(map(int, input().split()))
# tmp = []
# target = 1
# for i in wait:
# 	tmp.append(i)
# 	while tmp and tmp[-1] == target: # tmp 스택 하나로 비교
# 		tmp.pop()
# 		target += 1
# 	if len(tmp) > 1 and tmp[-1] > tmp[-2]:
# 		print("Sad")
# 		sys.exit()
# if tmp:
# 	print("Sad")
# else:
# 	print("Nice")
# n = int(input())
# start = list(map(int, input().split()))
# to = []
# temp = []
# cnt = 1
# flag = True
# startF = True
# while flag:
#     if len(start) == 0 and len(temp) == 0:
#         print("Nice")
#         break
#     if startF: #처음 시작
#         for i in range(max(len(start),len(temp))):
#             if start[i] != cnt:
#                 print("start[i] != cnt:",start)
#                 temp.append(start[i])
#                 del start[i]
#             else:
#                 print("else:",start)
#                 del start[i]
#                 cnt += 1
#                 startF = False
#                 break #for문 탈출
#     else:
#         if temp[i] == cnt:
#             print("if temp[i] == cnt:",start)
#             del temp[i]
#         elif start[i] == cnt:
#             print("elif start[i] == cnt:",start)
#             del start[i]
#         else:
#             print("Sad",start)
#             flag = False
#             break            

# #test
# # temp = [1,2,3]
# # del temp[1]
# # print(temp)