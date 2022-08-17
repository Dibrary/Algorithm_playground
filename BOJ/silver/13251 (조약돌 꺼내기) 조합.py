
'''
문제 이해가 어렵다.

조약돌이 5 6 7로 주어지면, 실제 총 돌멩이는 18개 있는 셈이다.
M은 왜 주어지는겨?


'''

# import sys
# input = sys.stdin.readline
#
# m = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
#
# total_count = sum(arr)
#
# result = 0
#
# for x in arr:
#     tmp = 1
#     for n in range(k):
#         print(x, n, x-n, total_count-n )
#         if x-n > 0:
#             upper = x-n
#             tmp *= (upper/(total_count-n))
#         else:
#             break
#     result += tmp
#     print(tmp)

# 위 코드는 틀림.

# m = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
#
# total_count = sum(arr)
#
# result = 0
#
# for x in arr:
#     tmp = 1
#     for n in range(k):
#         if x-n > 0:
#             upper = x-n
#             tmp *= (upper/(total_count-n))
#         else:
#             break
#     result += tmp
# print(result)
# 위 방식으로 계산하면 소수점 4째자리부터 예제 4번이 달라진다.


# from decimal import Decimal
#
# m = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
#
# total_count = sum(arr)
#
# result = 0
#
# for x in arr:
#     tmp = 1
#     for n in range(k):
#         if x-n > 0:
#             tmp *= (Decimal(str(x-n))/Decimal(str(total_count-n)))
#         else:
#             break
#     result += tmp
# print(result) # 근데 이렇게 계산한 것도 역시 4번째 예제에서 값이 다르다.



from decimal import Decimal

m = int(input())
arr = list(map(int, input().split()))
k = int(input())

total_count = sum(arr)

result = 0

for x in arr:
    tmp = 1
    flag = 0
    for n in range(k):
        if x - (k-1) < 0:
            flag = 1
            break
        else:
            tmp *= (Decimal(str(x-n))/Decimal(str(total_count-n)))
    if flag == 0:
        result += tmp
print(result) # k가 조약돌 갯수보다 많으면 해당 경우의 수는 모조리 0으로 취급해야 한다. (이거 때문에 예제 4번이 안맞았던 것)



## 다른 사람 코드 ##

import sys

M = int(sys.stdin.readline())
count = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
total = sum(count)


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


special = 0
for number in count:
    if number - K < 0:
        continue
    a = factorial(number) / factorial(number - K)
    b = factorial(total) / factorial(total - K)
    special += a / b

print(special)







import sys
import math

M = int(sys.stdin.readline())
stone = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
N = sum(stone)

total = math.comb(N, K) # comb라는 함수는 파이썬 3.8부터 나옴.
# comb 함수는 nCk 값을 반환한다. (n개의 수에서 k개를 선택)

same_color = 0
for s in stone:
    same_color += math.comb(s, K)

print(same_color/total)







from math import comb as c
m = int(input())
l = [ *map(int, input().split())]
s = sum(l)
k = int(input())
print(sum(c(i, k)/c(s, k)for i in l))








import sys
input = sys.stdin.readline
import math

M = int(input())
stones = list(map(int, input().split()))
K = int(input())
N = sum(stones)

total = math.comb(N, K)
same = 0
for s in stones:
    same += math.comb(s, K)

print(same / total)