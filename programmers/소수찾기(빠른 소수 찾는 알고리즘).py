# sympy 함수 못씀

import math

# def solution(n):
#     sheve = [x for x in range(1000001)]
#     sheve[1] = 0
#
#     for s in sheve[2:]:
#         for k in range(2, 1000000): # 이렇게 해 버리면 시간초과 됨.
#             if s * k < len(sheve):
#                 sheve[s * k] = 0
#
#     cnt = 0
#     for k in range(n):
#         if sheve[k] != 0:
#             cnt += 1
#     return cnt
#################################################################

import math
def solution(n):
    table = [n for n in range(1000001)]
    for i in range(2, int(math.sqrt(1000000))):
        for k in range(2, int(math.sqrt(1000000))):
            if i * k <= len(table):
                table[i * k] = 0
    table[1] = 0

    # cnt = 0
    # for k in range(n):
    #     if table[k] != 0:
    #         cnt += 1

    return len(table[:n + 1]) - table[:n + 1].count(0) # 이렇게 하면 갯수 나온다.

    return cnt

# 총 12개 문제 중에 5개 통과. 효율성 테스트 0개 통과

# 빠른 소수 찾는 알고리즘을 확인해 보니
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return len([2] + [2*i+1 for i in range(1,n//2) if sieve[i]])
# 우선 이게 하나 나왔다. 근데 n+1로 실행해야 n+1까지의 숫자를 포함한다.


### 다른 사람 구현 ###

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


### 다른 사람 구현 ###

def numberOfPrime(n):
    def isprime(m):
        for i in range(3, round(m **0.5)+1, 2):
            if(m % i is 0):
                return False
        return True
    return len([i for i in range(2, n+1) if(i is 2 or isprime(i) and i%2 is not 0)])

