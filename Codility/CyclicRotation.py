
# def solution(A, K):
#     result = [0 for _ in range(len(A))]
#
#     for idx, x in enumerate(A):
#         if idx + K < len(A):
#             result[idx+K] = x
#         else:
#             result[idx+K-len(A)] = x
#     return result

# 위 코드는 62% 받은 코드, K가 len(A)보다 클 경우 IndexError가 난다.


# def solution(A, K):
#     if K > len(A):
#         K = K%len(A)
#     result = [0 for _ in range(len(A))]
#
#     for idx, x in enumerate(A):
#         if idx + K < len(A):
#             result[idx+K] = x
#         else:
#             result[idx+K-len(A)] = x
#     return result

# 위 코드는 87% 받은 코드. ZeroDivisionError: integer division or modulo by zero가 남

def solution(A, K):
    if A == []:
        return []
    if K > len(A):
        K = K%len(A)
    result = [0 for _ in range(len(A))]

    for idx, x in enumerate(A):
        if idx + K < len(A):
            result[idx+K] = x
        else:
            result[idx+K-len(A)] = x
    return result



print(solution([3,8,9,7,6],3))
print(solution([3,8,9,7,6],-3))
print(solution([1,2,3,4],4))



