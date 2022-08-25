

def get_divisor(n): # 약수 구하는 함수.
    n = int(n)
    divisors = []

    for i in range(1, n + 1):
        if (n % i == 0):
            divisors.append(i)

    return divisors

def solution(left, right):
    result = 0

    for x in range(left, right+1):
        if len(get_divisor(x))%2 == 0:
            result += x
        else:
            result -= x
    return result


## 다른 사람 코드 ##

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer








def solution(left, right):
    def cnt_yak(number):
        cnt = 1
        for i in range(1, number//2+1):
            if number % i == 0:
                cnt += 1
        return cnt

    answer = 0
    for i in range(left, right+1):
        cnt = cnt_yak(i)
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer