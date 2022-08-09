
'''
최대공약수 = 두 값이 가지고 있는 약수 중 가장 큰 값.
'''
# import sys
# sys.setrecursionlimit(10**6)
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)
#
# a, b = map(int, input().split())
# a = int("1"*a) # 갯수만큼 1을 만들어놓고 해버리면 메모리 차지 엄청남.
# b = int("1"*b)
#
# if b == 0:
#     print(a)
# else:
#     print(gcd(min(a,b), max(a,b)%min(a,b)))

# 위 코드는 2번째 예제까지 됨. 3번째 예제는 MemoryError 발생함.

# import sys
# sys.setrecursionlimit(10**6) # 이 코드가 메모리 잡아먹는듯.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())

if b == 0:
    print("1"*a)
else:
    print("1"*gcd(min(a,b), max(a,b)%min(a,b)))
# 메모리 초과 걸림. # setrecursionlimit 지우고 통과됨.

## 다른 사람 코드 ##

import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

A, B = map(int, input().split())
digits = gcd(A, B)
result = ''
for _ in range(digits):
    result += '1'
print(result)









import sys
import math
input = sys.stdin.readline

a, b = map(int,input().split())
while b != 0:
    r = a % b
    a = b
    b = r

print("1"*a)

