

'''
문제 이해가 안 된다. 어떤 문서가 몇 번째로 인쇄되는지를 출력해야 하는 건가.?

숫자가 큰 게 중요도가 더 높은 것. = 먼저 나와야 할 것.

내가 생각한 핵심 아이디어는 위치를 기억하는 '변수'가 하나 더 있어야 한다는 것.

'''

from collections import deque

s = int(input())

for _ in range(s):
    n, m = map(int, input().split()) # n은 문서 갯수, m은 궁금한 문서 위치 index
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        print(1)
    else:
        tmp = [0 for _ in range(len(arr))]
        tmp[m] = 1
        tmp = deque(tmp)

        values = deque(arr)

        cnt = 0

        while values != []:
            v = values.popleft()
            idx = tmp.popleft()

            # if sorted(list(values))[-1] > v: # 이렇게 할 필요 없다. max로 확인할 수 있음.
            if max(values) > v:
                values.append(v)
                tmp.append(idx)
            else:
                if idx == 1:
                    cnt += 1
                    print(cnt)
                    break
                else:
                    cnt += 1


# 위 코드는 런타임 에러가 난다.
# max(values)로 수정하고 나서는 ValueError 런타임 에러가 난다.

## 다른 사람 코드 ##
'''
imp의 첫번째 값이 최대값이 될 때까지 가장 첫 번째 값을 맨 뒤로 보내는 FIFO를 반복하고, 
첫번째 값이 최대값이 되면 order를 하나 증가시키는 것이다.
또한, 원래 문서의 인덱스를 idx에 저장해놓고 imp의 순서가 바뀔 때마다 같이 순서를 바꿔줘야만 한다. 
그래야 원래 m번째 문서가 언제 출력되는 지를 아니까!
'''

# test_cases = int(input())
#
# for _ in range(test_cases):
#     n, m = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     idx = list(range(len(imp))) # 숫자가 0부터 순서대로 들어간다.
#     idx[m] = 'target' # m 위치만 target이라고 변경.
#
#     # 순서
#     order = 0
#
#     while True:
#         # 첫번째 if: imp의 첫번째 값 = 최댓값?
#         if imp[0] == max(imp):
#             order += 1
#
#             # 두번째 if: idx의 첫 번째 값 = "target"?
#             if idx[0] == 'target':
#                 print(order)
#                 break
#             else:
#                 imp.pop(0)
#                 idx.pop(0)
#
#         else:
#             imp.append(imp.pop(0))
#             idx.append(idx.pop(0))



