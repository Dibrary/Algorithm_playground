from collections import deque

# def solution(priorities, location):
#     target = priorities[location]
#     q = deque(priorities)
#     cnt = 0
#     while q:
#         value = q.popleft()
#         if sorted(list(q))[-1] > value:
#             q.append(value)
#         else:
#             if value == target:
#                 cnt += 1
#                 return cnt
#             else:
#                 cnt += 1

# print(solution([2,1,3,2],2))
# print(solution([1,1,9,1,1,1],0))

## 위 방식대로 하면 같은 우선순위의 경우에 한해서 구할 수 없음.
from collections import deque


# def solution(priorities, location):
#     flag = [0 for _ in range(len(priorities))]
#     flag[location] = 1
#     temp = deque(flag)
#
#     target = priorities[location]
#     q = deque(priorities)
#
#     cnt = 0
#
#     while q:
#         value = q.popleft()
#         idx = temp.popleft()
#
#         if sorted(list(q))[-1] > value:
#             q.append(value)
#             temp.append(idx)
#         else:
#             if value == target and idx == 1:
#                 cnt += 1
#                 return cnt
#             else:
#                 cnt += 1

# 위 방식으로 하면 3개는 통과하지 않는다.
# if조건문에서 걸리는 듯
# print(solution([7,5,9,4,2,6,1,8,3],6)) 이렇게 하면 list index out of range 에러남.

# print(solution([2,1,3,2],2))
# print(solution([1,1,9,1,1,1],0))

from collections import deque


def solution(priorities, location):
    flag = [0 for _ in range(len(priorities))]
    flag[location] = 1
    temp = deque(flag)

    q = deque(priorities)

    cnt = 0

    while q:
        if len(q) != 0:
            if max(q) > q[0]:
                q.append(q.popleft())
                temp.append(temp.popleft())
            else:
                cnt += 1
                if temp[0] == 1:
                    return cnt
                else:
                    q.popleft()
                    temp.popleft() # 값을 제거해야함.
        else:
            return cnt

# 이렇게 바꾸면 런타임에러 문구가 '실패'로만 바뀐다.

print(solution([7,6,3,6,2,1],3))
print(solution([7,5,9,4,2,6,1,8,3],6))