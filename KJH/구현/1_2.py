#길이를 맞추는 작업 중
def func_a(string, length):
    padZero = ""
    #최대길이 - 더 작은 문자열의 길이 -> 문자열 길이 차이값 
    padSize = length - len(string)
    #부족한 사이즈만큼 for문을 돌면서 0을 추가함
    for i in range(padSize):
        padZero += "0"
    #사이즈가 같아진 문자열을 return
    return padZero + string

def solution(binaryA, binaryB):
    #더 긴 문자열의 길이를 측정하여 변수에 저장
    max_length = max(len(binaryA), len(binaryB))
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length)
    
    hamming_distance = 0
    #for문을 돌며 둘의 값이 같지 않게된 순간 1을 누적해서 더함
    for i in range(max_length):
        if binaryA[i] != binaryB[i]:
            hamming_distance += 1
    return hamming_distance

#test
binaryA = "10010"
binaryB = "110"
print(solution(binaryA, binaryB))
