
import math

n = int(input())
if n == 1:
    pass
else:
    values = [] # 내가 짠 코드는 굳이 불필요하게 담아서 나중에 반복문을 다시 돌리는 것에 있다.

    for i in range(2, n):
        while n%i == 0:
            values.append(i)
            n = n//i
    if values == []: # 2,3,5,7 같은 소수의 경우는 이렇게 처리.
        print(n)
    else:
        for k in values:
            print(k)

# 시간이 굉장히 오래 걸린다.

### 다른 사람의 코드
import math

N = int(input())

def func(num):
    if num == 1:
        return ''
    for i in range(2, math.trunc(math.sqrt(num)+1)):
        if num%i == 0:
            print(i)
            return func(num//i)
    return num

print(func(N))

### 다른 사람의 코드 2

N = int(input())
d = 2
t = int(N**0.5)
while d <= t:
    if N % d == 0:
        print(d)
        N = N//d
    else:
        d += 1
if N>1:
    print(N)