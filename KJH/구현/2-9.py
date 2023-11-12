def solution(password):
    length = len(password)
    for i in range(length - 2):
        #1 0
        first_check  = ord(password[i + 1]) - ord(password[i])
        #2 1
        second_check = ord(password[i]) - ord(password[i+1])
        second_check = ord(password[i+2]) - ord(password[i+1]) #수정 부분
        if first_check == second_check and (first_check == 1 or first_check == -1):
            return False
    return True

password1 = "cospro890"
print(solution(password1))

password2 = "cba323"
print(solution(password2))