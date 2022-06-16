
'''
문제만 보고 왜 BFS를 써야 하는지 이해가 잘 안됨.
(BFS는 visited 처리 안 해도 됨)

총 3가지 경우에 대해 queue에 넣는다면, 3가지 포인트에 대해 도달 거리가 나올거고, 그 중에 가장 먼저 도달하는 것이 나올 것?

'''

# from collections import deque
#
# n, k = map(int, input().split())
#
# def bfs(x, cnt, target):
#     q = deque([x])
#
#     dx = [2, 1, -1]
#
#     while q:
#         now = q.popleft()
#         for i in range(3):
#             if i == 0:
#                 nx = now*dx[i]
#             else:
#                 nx = now+dx[i]
#                 if abs(now-target) > abs(nx-target):
#                     q.append(nx)
#                     cnt += 1
#                     print(nx)
#     return cnt
#
#
# answer = bfs(n, 0, k) # 처음 횟수는 0
# print(answer)


########################################################

from collections import deque

# n, k = map(int, input().split())
#
# def bfs(x, cnt, target):
#     q = deque([x])
#
#     dx = [2, 1, -1]
#
#     while q:
#         now = q.popleft()
#         first = now + 1
#         second = now - 1
#         third = now * 2
#         # if abs(first-target) < abs(second-target) and abs(first-target) < abs(third - target):
#         #     q.append(first)
#         #     cnt += 1
#         # elif abs(first-target) < abs(second-target) and abs(first-target) > abs(third - target):
#         #     q.append(third)
#         #     cnt += 1
#         # elif abs(second-target) < abs(first-target) and  abs(second-target) < abs(third - target):
#         #     q.append(second)
#         #     cnt += 1
#         # elif abs(second-target) < abs(first-target) and  abs(second-target) > abs(third - target):
#         #     q.append(third)
#         #     cnt += 1 # 조건을 모조리 작성하는건 시간낭비;;
#
#
#     return cnt
#
#
# answer = bfs(n, 0, k) # 처음 횟수는 0
# print(answer)

########################################################


# from collections import deque
#
# n, k = map(int, input().split())
#
# def bfs(x, cnt, target):
#     q = deque([x])
#
#     while q:
#         now = q.popleft()
#         if now == target:
#             break
#         first = now + 1
#         second = now - 1
#         third = now * 2
#         min_distance = min(abs(first-target), abs(second-target), abs(third-target))
#         if min_distance == abs(first-target):
#             q.append(first)
#         elif min_distance == abs(second-target):
#             q.append(second)
#         elif min_distance == abs(third-target):
#             q.append(third)
#         print(now, cnt)
#         cnt += 1
#
#     return cnt
#
#
# answer = bfs(n, 0, k) # 처음 횟수는 0
# print(answer-1) # -1을 해야 예제와 같은데...

# 2%에서 곧바로 틀림 ########################################################





### 다른 사람 코드 ###

from collections import deque

MAX = 100000
dist = [0]*(MAX+1)
n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)
        print(dist, nx, q)
bfs()

### 다른 사람 코드 ###

# from collections import deque
#
#
# def solve(n, k):
#     time = [0] * (200001)
#     q = deque([n])
#     time[n] = 0
#
#     while q:
#         now = q.popleft()
#         if now == k:
#             print(time[k])
#             return
#
#         if abs(k - now) > abs(k - 2 * now) and time[2 * now] == 0:
#             q.append(2 * now)
#             time[2 * now] = time[now] + 1
#
#         if now + 1 <= 100000 and time[now + 1] == 0:
#             q.append(now + 1)
#             time[now + 1] = time[now] + 1
#
#         if now - 1 >= 0 and time[now - 1] == 0:
#             q.append(now - 1)
#             time[now - 1] = time[now] + 1
#
#
# n, k = map(int, input().split())
# solve(n, k)