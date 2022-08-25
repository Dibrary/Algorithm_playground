

# def solution(n):
#     result = 0
#     tmp = []
#     for i in range(1, n//2+1):
#         if n%i == 0 and i not in tmp and n//i not in tmp:
#             tmp.append(i)
#             tmp.append(n//i)
#             result += (i + n//i)
#     return result

# 위 코드는 17개 문제 중에 3개 틀림.


def get_divisor(n): # 약수 구하는 함수.
    n = int(n)
    divisors = []

    for i in range(1, n + 1):
        if (n % i == 0):
            divisors.append(i)

    return divisors

def solution(n):
    return sum(get_divisor(n))
# 위 코드로 통과됨.


## 다른 사람 코드 ##

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])









from math import sqrt

def sumDivisor(num):
    answer = 0
    for d in range(1, int(sqrt(num))+1):
        if num%d == 0:
            answer += d
            answer += int(num/d)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
