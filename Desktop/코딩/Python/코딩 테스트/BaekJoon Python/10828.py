# import sys
# #input = sys.stdin.readline
# n = int(sys.stdin.readline())
# lst = []
# for _ in range(n):
#     MyStr = sys.stdin.readline()
#     if 'push' in MyStr:
#         a,b = MyStr.split()
#         lst.append(int(b))
#     elif MyStr == 'pop':
#         if len(lst) != 0:
#             print(lst[-1])
#             lst.pop()
#         else:
#             print(-1)
#     elif MyStr == 'size':
#         print(len(lst))
#     elif MyStr == 'empty':
#         if len(lst) == 0:
#             print(1)
#         else:
#             print(0)
#     elif MyStr == 'top':
#         if len(lst) != 0:
#             print(lst[-1])
#         else:
#             print(-1)
import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    stack.append(command[1])
    
  elif command[0] == 'pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())
      
  elif command[0] == 'size':
    print(len(stack))
    
  elif command[0] == 'empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)