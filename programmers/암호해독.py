
def solution(cipher, code):
    cipher = "9"+cipher # for문이 0부터 시작해서 맨 앞에 그냥 아무거나 추가함.
    result = ""
    for x in range(0, len(cipher), code):
        result += cipher[x]
    return result[1:]

print(solution("dfjardstddetckdaccccdegk", 4))



## 다른 사람 코드 ##
def solution(cipher, code):
    answer = cipher[code-1::code] # code-1부터 code 간격별 값을 가져온다.
    return answer







def solution(cipher, code):
    output = ""
    for i in range(code - 1, len(cipher), code):
        output += cipher[i]
    return output