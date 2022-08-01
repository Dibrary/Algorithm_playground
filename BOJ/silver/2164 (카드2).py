from collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    value = q.popleft()
    q.append(value)
print(q.pop())


## 다른 사람 코드 ##

from collections import deque

num = int(input())
queue = deque(i+1 for i in range(num))
i = 0
while len(queue) > 1:
    if i % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    i += 1
print(queue[0])



