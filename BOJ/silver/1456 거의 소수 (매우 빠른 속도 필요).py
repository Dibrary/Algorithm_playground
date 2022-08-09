
'''
이 문제에서 주어지는 숫자의 범주는 10**14까지 가능..
즉, 그냥 for문가지고는 접근하면 안 됨.

먼저 떠오른 생각은.
소수를 먼저 찾아내고, 소수의 제곱이 주어진 A, B 범주에 들어가는지 체크하는 방법
'''

# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True
#
# a, b = map(int, input().split())
# result = 0
#
# for i in range(a, b+1):
#     if isPrime(i):
#         cnt = 2
#         while i**cnt <= b:
#             tmp = i**cnt
#             if tmp <= b:
#                 result += 1
#             else:
#                 continue
#             cnt += 1
# print(result)

# 위 코드는 시간초과로 실패.

'''
책 풀이

주어진 범주 10**14의 제곱근인 10**7까지의 소수를 미리 구해놓고, (10**7이상의 소수는 곱해버리면 10**14범주를 넘어선다.)
소수들의 제곱값이 범주에 들어가는지만 확인하면 된다. 라고 나오는데, 이 풀이는 Python으로는 너무 느린듯.
'''

# A = [x for x in range(2, 10000001)]
#
# for k in range(2, int(len(A)**0.5)+1):
#     if A[k] == 0:
#         continue
#     m = k+k
#     for m in range(k+k, len(A), m+k):
#         A[m] = 0
# 위 방식으로도 소수만 걸러낼 수 있다.

A = [x for x in range(2, 10000001)]

for k in range(2, int(len(A)**0.5)+1):
    if A[k] == 0:
        continue
    m = k+k
    for m in range(k+k, len(A), m+k):
        A[m] = 0

# 위 시빙은 time으로 계산했을 때, 5.16초 걸린다.
# isPrime 함수로 계산하면 시간이 너무 오래 걸린다.

a, b = map(int, input().split())
result = []

for i in range(a, b+1):
    if i == 1:
        continue
    if A[i] != 0:
        cnt = 2
        while i**cnt <= b:
            tmp = i**cnt
            if tmp <= b:
                result.append(tmp)
            else:
                continue
            cnt += 1
print(result)

# 3%에서 런타임에러 마주함 (IndexError).





## 다른 사람 코드 ##

N = 10 ** 7 + 5
sieve = [True] * (N + 100)
sieve[0] = False
sieve[1] = False
sieve[2] = True
prime = 2
while prime * prime <= N:
    if not sieve[prime]:
        prime += 1
        continue
    for t in range(2 * prime, N + 3, prime):
        sieve[t] = False
    prime += 1

# 위 시빙은 time으로 계산했을 때, 4.19초 걸린다.

A, B = map(int, input().split())
cnt = 0
for p in range(2, N):
    if not sieve[p]: continue
    mul = p * p
    while mul <= B:
        cnt += (A <= mul)
        mul *= p
print(cnt)

# 위 코드는 비교적 굉장히 빠르게 진행된다.


import math
from collections import deque
A, B = map(int, input().split())
sqrt_B = int(math.sqrt(B))

is_prime = [True for _ in range(sqrt_B+1)]
is_almost_prime = []

for i in range(2, sqrt_B+1):
    if is_prime[i]:
        for j in range(i+i, sqrt_B+1, i):
            if j <= B:
                is_prime[j] = False

for i in range(2, sqrt_B+1):
    if is_prime[i]:
        n = 2
        j = i**n
        while j <= B:
            if j >= A:
                is_almost_prime.append(j)
            n += 1
            j = i**n


is_almost_prime.sort()
is_almost_prime = deque(is_almost_prime)

print(len(is_almost_prime))









import sys
import math
a, b = map(int, sys.stdin.readline().split())

rb = int(b ** (1/2))
primes = [False, False] + [True] * (rb-1)
count = 0
for i in range(2, rb+1):
    # if i * i > rb:
    #     break
    if not primes[i]:
        continue
    for j in range(i*i, rb+1, i):
        primes[j] = False
ans = 0

for i in range(2, len(primes)):
    if primes[i]:
        tp = i*i
        while(tp <= b):
            if (a <= tp):
                ans += 1
            tp *= i

print(ans)











A, B = map(int, input().split())

sieve = [True] * (int(B ** 0.5) + 1)
sieve[0] = sieve[1] = False
for i in range(2, len(sieve)):
    if sieve[i]:
        for j in range(i + i, len(sieve), i):
            sieve[j] = 0

cnt = 0
for idx, is_prime in enumerate(sieve):
    if not is_prime:
        continue
    val = idx ** 2
    while val <= B:
        if A <= val <= B:
            cnt += 1
        val *= idx
print(cnt)