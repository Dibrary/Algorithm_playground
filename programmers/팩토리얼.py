
def solution(n):
    table = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    if n in table:
        return table.index(n)+1
    result = 0
    for x in range(11):
        if table[x] < n:
            result += 1
        else:
            break
    return result




## 다른 사람 코드 ##

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k





def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    answer -= 1
    return answer