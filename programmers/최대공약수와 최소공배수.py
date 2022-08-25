
def get_divisor(n): # 약수 구하는 함수.
    n = int(n)
    divisors = []

    for i in range(1, n + 1):
        if (n % i == 0):
            divisors.append(i)

    return divisors

def get_value(a, b): # 최소공배수 구하는 함수.
    for i in range(max(a, b), (a*b)+1):
        if i%a ==0  and i%b == 0:
            return i

def solution(n, m):
    first = max(set(get_divisor(n)) & set(get_divisor(m)))
    second = get_value(n, m)
    return [first, second]


## 다른 사람 코드 ##

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))









def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

def gcdlcm(a, b):
    answer = [gcd(a,b), lcm(a,b)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))