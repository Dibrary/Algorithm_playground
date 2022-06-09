
# 여기서 의문이 드는 점은, 앞으로 들어올 갯수가 몇 개인지 알고 새 데크를 만들어야 하는거 아니냐.. 싶다.
# 예제에서 3, 6을 별개의 데크로 만들었는데, 5와 4가 있다는 것을 '미리' 알아야 별개의 데크를 만들어야 한다는 것을 알텐데;;


# 인터넷에 C++로 된 코드를 파이썬으로 옮겨보았음.

n = int(input())

arr = []
sortedarr = []

result = 0

for _ in range(n):
    value = int(input())
    arr.append(value)
    sortedarr.append(value)

sortedarr.sort()
for i in range(n):
    for j in range(n):
        if arr[i] == sortedarr[j]:
            sortedarr[j] = 1001 # 여기를 == 으로 해 버리니 답이 안나오지 =_=';;
            break

    if j == 0:
        if sortedarr[j+1] != 1001:
            result += 1
    elif j == n-1:
        if sortedarr[j-1] != 1001:
            result += 1
    elif ((sortedarr[j-1] == 1001) or (sortedarr[j+1] == 1001)):
        continue
    else:
        result += 1
print(result)


## 다른 사람 코드 ##

def main():
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    order_by_num = {num: i for i, num in enumerate(sorted(set(nums)))}
    can_add = [False] * N
    answer = 0
    for num in nums:
        order = order_by_num[num]
        if not can_add[order]:
            answer += 1
        if order > 0:
            can_add[order - 1] = True
        if order < N - 1:
            can_add[order + 1] = True

    print(answer)


if __name__ == '__main__':
    main()

## 다른 사람 코드 ##
import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())
A = []
U = []
for i in range(0, N):
    A += [int(input())]

U = copy.deepcopy(A)
U.sort()
for i in range(0, N):
    A[i] = U.index(A[i])

res = 0
v = [False] * 50
for i in range(0, N):
    v[A[i]] = True
    newDeque = True
    if A[i] - 1 >= 0 and v[A[i] - 1]:
        newDeque = False
    if A[i] + 1 < N and v[A[i] + 1]:
        newDeque = False
    if newDeque:
        res += 1
print(res)