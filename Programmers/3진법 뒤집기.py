
# def solution(n):
#     result = ""
#     while n > 3:
#         result = str(n % 3) + result
#         n = n // 3
#     result = str(n) + result
#
#     answer = 0
#     for i in range(len(result)):
#         answer += int(result[i])*(3**i)
#     return answer


# 3번과 7번을 통과하지 못한다.


def solution(n):
    result = ""
    while n >= 3: # 여기에 == 이 들어가는 것이 중요하다.
        result = str(n % 3) + result
        n = n // 3
    result = str(n) + result

    answer = 0
    for i in range(len(result)):
        answer += int(result[i])*(3**i)
    return answer

print(solution(125))
print(solution(45))

## 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer