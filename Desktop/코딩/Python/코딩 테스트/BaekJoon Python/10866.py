# n = int(input())
# deque = []
# for _ in range(n):
#     command = input().split()
#     if command[0] == 'push_back':
#         deque.append(command[1])
#     elif command[0] == 'push_front':
#         for i in range(len(deque)-1,-1,-1):
#             deque[i] = deque[i-1]
#         deque[0] = command[1]
    
#     elif command[0] == 'pop_front':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#             del deque[0]
        
#     elif command[0] == 'pop_back':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[-1])
#             deque.pop()

#     elif command[0] == 'size':
#         print(len(deque))

#     elif command[0] == 'empty':
#         if len(deque) == 0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[0])
#     elif command[0] == 'back':
#         if len(deque) == 0:
#             print(-1)
#         else:
#             print(deque[-1])
lst = [1]
for i in range(1, -1, -1):
    lst[i] = lst[0]