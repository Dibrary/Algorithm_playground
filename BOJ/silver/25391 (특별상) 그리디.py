
'''
이건 그리디 같은 느낌이 나는데, 수학도 좀 섞여 있는 것 같다.

'''

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
scores = []

for _ in range(n):
    a, b = map(int, input().split())
    scores.append((a, b))

ban = []
total = 0

scores.sort(key = lambda x: (-x[1]))

for s in range(k):
    total += scores[s][0]
    ban.append(scores[s][1])

scores.sort(key = lambda x: (-x[0]))

idx = 0
while m > 0:
    if scores[idx][1] not in ban:
        total += scores[idx][0]
        m -= 1
    idx += 1

print(total)

# 16%에서 시간초과 걸린다.





