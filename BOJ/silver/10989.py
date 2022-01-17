
dk = dict()
sys.getsizeof(dk)
for i in range(1, 10001):
    dk[i] = 1
sys.getsizeof(dk)

# 사전을 쓰면 메모리 크기가 295008 나옴

a = [0]*10001 # 이렇게 하면 메모리 크기가 80072 나온다.

import sys
n = int(input())

tmp = [0]*10001

for i in range(0, n):
    value = int(sys.stdin.readline())
    tmp[value] += 1

for idx in range(0, len(tmp)):
    if tmp[idx] != 0:
        for j in range(0, tmp[idx]):
            print(idx)
