
'''
수열의 합을 구하겠다.

두 수를 묶으려 한다.
"같은 위치의 수를 묶는건 불가능." 이게 무슨말일까?

'''
# 반례 = 음수 2개를 곱하면 양수가 될 수 있다.
# 반례 = 음수와 0을 곱하면 0이 된다.
# 반례 = 양수 2개를 곱한다고 값이 늘어나는 게 아닐 수 있다. (2*1 = 2, 2+1 = 3)

'''
1보다 낮은 두 수를 곱하면 항상 양수가 됨.
1보다 큰 두 수를 곱하면 항상 양수.
'''

n = int(input())

minor = []
zero = []
ones = []
plus = []

for _ in range(n):
    value = int(input())
    if value < 0:
        minor.append(value)
    elif value > 1:
        plus.append(value)
    elif value == 0:
        zero.append(value)
    elif value == 1:
        ones.append(value)

minor.sort()
plus.sort(reverse=True)

minor_sum = 0
before = 0
for i in minor:
    if before == 0:
        before = i
    else:
        minor_sum += (before * i)
        before = 0
if before != 0 and len(zero) == 0:
    minor_sum += before

plus_sum = 0
before = 0
for k in plus:
    if before == 0:
        before = k
    else:
        plus_sum += (before * k)
        before = 0
if before != 0:
    plus_sum += before

print(plus_sum + minor_sum + len(ones))

# 26%에서 AttributeError로 틀림 (오타 있었다.)


## 다른 사람 코드 ##

import sys
input = sys.stdin.readline

N=int(input())
nums = [int(input()) for i in range(N)]
neg = []; pos = []; zero = 0
res = 0
for i in nums:
    if i < 0: neg.append(i)
    if i > 0: pos.append(i)
    if i == 0: zero += 1
neg.sort(); pos.sort(reverse=True)
for i in range(len(neg) // 2):
        res += neg[i*2] * neg[i*2+1]
if len(neg) % 2 and zero == 0: res += neg[-1]
for i in range(len(pos) // 2):
    if pos[i*2] == 1 or pos[i*2+1] == 1:
        res += pos[i*2] + pos[i*2+1]
    else: res += pos[i*2] * pos[i*2+1]
if len(pos) % 2: res += pos[-1]

print(res)










import sys
input = sys.stdin.readline

n = int(input()) # 1<=n<=50
# 요소가 음수면 묶지 않아야 하고 큰수끼리 묶으면 값이 더 커진다. 묶는 것은 두개의 수를 대상으로 가능하고 모든 수는 한번만 묶을 수 있다.
# 음수 * 음수  //  음수 + 양수  //  양수 * 양수
# 0 * 음수  //  0 + 양수
# 1 + 양수  //  1 + 음수
negativeNum = []
positiveNum = []
cnt = 0
for i in range(n):
    num = int(input())
    if num <= 0:
        negativeNum.append(num)
    else:
        positiveNum.append(num)
     # 각 요소는 -1000이상 1000이하
positiveNum.sort()
negativeNum.sort(reverse=True)
res = 0

while len(positiveNum) >= 2:
    x = positiveNum.pop()
    y = positiveNum.pop()

    if x == 1 or y == 1:
        res += x + y
    else:
        res += x * y
if positiveNum:
    res += positiveNum.pop()

while len(negativeNum) >= 2:
    x = negativeNum.pop()
    y = negativeNum.pop()

    res += x * y
if negativeNum:
    res += negativeNum.pop()

print(res)










t = int(input())
p = []
n = []
o = []
s = 0
for _ in range(t):
    num = int(input())
    if num > 1:
        p.append(num)
    elif num <= 0:
        n.append(num)
    else:
        o.append(num)

p.sort(reverse = True)
n.sort()
answer = 0
if len(p) % 2 == 0:
    for i in range(0,len(p),2):
        answer  += p[i] * p[i+1]
else:
    for i in range(0,len(p)-1,2):
        answer += p[i] * p[i+1]
    answer  += p[len(p)-1]
if len(n) % 2 == 0:
    for i in range(0,len(n),2):
        answer  += n[i] * n[i+1]
else:
    for i in range(0,len(n)-1,2):
        answer  += n[i] * n[i+1]
    answer  += n[len(n)-1]
answer += sum(o)

print(answer)















mi = []
pl = []
ans = 0
n = int(input())

for i in range(n):
    num = int(input())
    if num <= 0:
        mi.append(num)
    if num > 0:
        pl.append(num)

mi.sort(reverse=True)  # 내림차순 정렬
pl.sort()  # 오름차순 정렬
# -> pop() 하면 마지막 요소부터 빠지기 때문 : 큰 숫자 먼저 곱해주기
while 1:
    if len(mi) == 0:
        break

    a = mi.pop()
    if len(mi) == 0:
        ans += a
        break
    b = mi.pop()

    ans += (a * b)

while 1:
    if len(pl) == 0:
        break

    a = pl.pop()
    if len(pl) == 0:
        ans += a
        break
    b = pl.pop()

    if a > 1 and b > 1:
        ans += (a * b)
    else:
        ans += (a + b)
print(ans)