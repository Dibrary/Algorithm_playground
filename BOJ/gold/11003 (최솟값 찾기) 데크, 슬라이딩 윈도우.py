
'''
문제에서 최솟값을 구하는 범위가 i-L+1까지 이므로 L로 생각하면 된다.

정렬은 O(nlogn)의 복잡도를 가지는데, N, L 최대 범위가 5000000까지 이므로 O(n)안에 풀 수 있어야 함.
L을 리스트로 해버리면 시간이 너무 오래 걸려버림.

우선순위 큐를 써도 되낭?
'''

# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# arr = list(map(int, input().split()))
#
# for k in range(1, L):
#     print(min(arr[:k]))
# for i in range(len(arr)-L+1):
#     print(min(arr[i:i+L]))

# 위 방식은 13%에서 시간초과

import sys
input = sys.stdin.readline
from collections import deque
q = deque()
N, L = map(int, input().split())
arr = list(map(int, input().split()))

result = ""
for i in range(len(arr)):
    if len(q) == 0:
        q.append((i + 1, arr[i]))
    else:
        while len(q) != 0 and q[-1][1] > arr[i]:
            q.pop()
        q.append((i + 1, arr[i]))

        if q[-1][0] - q[0][0] == L:
            q.popleft()
    result += str(q[0][1])
print(" ".join(map(str, result)))

## 위 코드 시간초과 걸린다








## 다른 사람 코드 ##

from collections import deque
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
d = [0 for _ in range(N)]

q = deque()

for idx in range(N):
    while q and q[-1][1] > arr[idx]:
        q.pop()
    while q and idx - q[0][0] >= 1:
        q.popleft()
    q.append((idx, arr[idx]))
    d[idx] = q[0][1]
print(*d)

# 틀렸다고 함. 왜지?


from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
q = deque()
ans = []
for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()
    while q and q[0][1] < i - k + 1:
        q.popleft()
    q.append((arr[i],i))
    print(q[0][0], end = ' ')

# 진행하는데 엄청 오래걸림.


from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
D = []
window = deque()  # window의 가장 앞 원소를 최솟값으로 유지하기!!


for i in range(N):
    # 새로 들어올 친구가 window의 마지막 원소부터 차례로 확인하면서 본인보다 작으면 제거해준다.
    while window and window[-1][1] > arr[i]:
        window.pop()


    # 현재 확인하고 있는 window의 길이가 L과 같은 경우 가장 앞의 원소를 제거해준다.
    if window and  i - window[0][0] == L:
        window.popleft()


    # 원소를 window에 추가하고
    window.append((i, arr[i]))
    D.append(window[0][1])  # window의 가장 앞 원소가 최솟값으로 유지되고 있으므로 이를
                            # D배열에 append 함!

print(*D)