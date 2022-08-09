
# t = int(input())
#
# for _ in range(t):
#     a, b = map(int, input().split())
#     while a%b != 0:
#         tmp = b
#         b = a % b
#         a = tmp
#     print(b)

# 위 코드 틀림

import copy

t = int(input())

for _ in range(t):
    fa, fb = map(int, input().split())
    a = copy.deepcopy(fa)
    b = copy.deepcopy(fb)

    while b%a != 0:
        tmp = a
        a = b % a
        b = tmp
    print((fa//a) * (fb//a) * a)




## 다른 사람 코드 ##

T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    X = A * B
    while A != 0:
        r = B % A
        B = A
        A = r
    print(round(X/B))







t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    A, B = a, b
    while b != 0:
        a, b = b, a % b

    print(A * B // a)







T = int(input())

def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)

def LCI(A, B):
    return A * B // GCD(A, B)

while T:
    A, B = map(int, input().split(' '))

    print(A * B // GCD(A, B))

    T -= 1








import sys

n = int(sys.stdin.readline())

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return(gcd(y,x%y))

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    k = gcd(a,b)
    print(a*b//k)