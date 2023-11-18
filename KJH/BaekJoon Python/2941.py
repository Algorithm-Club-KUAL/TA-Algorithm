n = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=',] #8개
cnt = 0
# for i in range(8):
#     n = n.replace(lst[i], ".")
# print(len(n))

for i in range(8):
    if lst[i] in n:
        print(f"n의 값: {n}")
        print(f"lst[i]의 값: {lst[i]}")
        n = n.replace(lst[i],"")
        cnt += 1
        
print(cnt)

# # #Debug
# n = "ljes=njak"
# if "lj" in n:
#     print("안녕")
# # # lst = ["lj"]

# #n = n.replace("lj","")
# #print(n)
# # # if n in lst[0]:
# # #     print("안녕")