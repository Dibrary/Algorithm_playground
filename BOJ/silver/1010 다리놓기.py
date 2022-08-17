n = int(input())

for _ in range(n):
    n, m = list(map(int, input().split()))

    up = {x for x in range(1, m + 1)}
    r = {x for x in range(1, n + 1)}
    n_r = {x for x in range(1, m - n + 1)}

    up_value = up - r
    tmp = up_value & n_r
    n_r = n_r - tmp
    up_value = up_value - tmp

    up_total, down_total = 1, 1
    for k in up_value:
        up_total *= k
    for j in n_r:
        down_total *= j
    print(int(up_total / down_total))

## 다른 사람 코드 ##
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))













def bridge(N, M):
    redundancy = M - N
    top = 1
    bottom = 1
    MN = 1
    for i in range(1, M + 1):
        top *= i
    for j in range(1, N + 1):
        bottom *= j
    for k in range(1, redundancy + 1):
        MN *= k
    return int(top / (bottom * MN))


N = int(input())
for i in range(N):
    N, M = map(int, input().split())
    print(bridge(N, M))









def fac(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp

def Com(m, n):
    return fac(m) // (fac(m - n) * fac(n))

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(Com(m, n))