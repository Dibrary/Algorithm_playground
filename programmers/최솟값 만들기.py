# def solution(A, B):
#     A.sort()
#     B.sort()
#
#     result = 0
#     for a, b in zip(A, B):
#         result = result + (a * b)
#     return result

# 위 코드 틀림
# 최소값은 A오름, B내림 정렬한 것 외에 A내림, B오름 정렬 한 것도 가능하다.


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    result = 0
    for a, b in zip(A, B):
        result = result + (a * b)

    A.sort(reverse=True)
    B.sort()

    result2 = 0
    for a, b in zip(A, B):
        result2 = result2 + (a * b)

    return min(result, result2)

# 다만 코드가 중복되는 부분이 있어서 좀 그렇다.
def calc(A, B):
    result = 0
    for a, b in zip(A, B):
        result = result + (a * b)
    return result

def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    result = calc(A, B)

    A.sort(reverse=True)
    B.sort()
    result2 = calc(A, B)

    return min(result, result2)

## 다른 사람 코드 ##

def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
# 위 코드는 개편되기 전인듯? A에 B reverse만 하면 안됨.


