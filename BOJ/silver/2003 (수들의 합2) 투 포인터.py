
'''
범주를 초과해도 slicing이 가능한 방법을 찾아야 한다.

'''

# from collections import deque
#
# n, m = map(int, input().split()) # 전체 숫자 갯수는 10000개를 넘지 않는다.
# arr = list(map(int, input().split()))
#
# total = deque()
# total.append(arr[0]) # 첫번째 값 넣어놓고 시작.
#
# start_idx = 0
# end_idx = 0
#
# cnt = 0
# while start_idx <= end_idx:
#     if sum(total) < m:
#         end_idx += 1
#         total.append(arr[end_idx])
#     elif sum(total) == m:
#         cnt += 1
#         end_idx += 1
#         total.append(arr[end_idx])
#     elif sum(total) > m:
#         start_idx += 1
#         total.popleft()
# print(cnt)







# from collections import deque
#
# n, m = map(int, input().split())  # 전체 숫자 갯수는 10000개를 넘지 않는다.
# arr = list(map(int, input().split()))
#
# total = deque()
# total.append(arr[0])  # 첫번째 값 넣어놓고 시작.
#
# start_idx = 0
# end_idx = 0
#
# cnt = 0
# while start_idx <= end_idx:
#     if sum(total) < m: # 항상 값을 전부 다시 계산하므로 효율적이지 않다.
#         if end_idx == len(arr) - 1:
#             start_idx += 1
#             total.popleft()
#         else:
#             end_idx += 1
#             total.append(arr[end_idx])
#     elif sum(total) == m:
#         cnt += 1
#         if end_idx == len(arr) - 1:
#             start_idx += 1
#             total.popleft()
#         else:
#             end_idx += 1
#             total.append(arr[end_idx])
#     elif sum(total) > m:
#         start_idx += 1
#         total.popleft()
#
# print(cnt)

# 64%에서 틀림







n, m = map(int, input().split())  # 전체 숫자 갯수는 10000개를 넘지 않는다.
arr = list(map(int, input().split()))

total = arr[0]  # 첫번째 값 넣어놓고 시작.

start_idx = 0
end_idx = 0

cnt = 0

while start_idx <= end_idx:
    if total < m:
        if end_idx == len(arr) - 1:
            total -= arr[start_idx] # 이렇게 하면 범주를 초과해버리는 순간 에러 남.
            start_idx += 1
        else:
            end_idx += 1
            total += arr[end_idx]
    elif total == m:
        cnt += 1
        if end_idx == len(arr) - 1:
            total -= arr[start_idx]
            start_idx += 1
        else:
            end_idx += 1
            total += arr[end_idx]
    elif total > m:
        total -= arr[start_idx]
        start_idx += 1

print(cnt)

# 위 코드는 좀 더 빨리 진행되지만 역시 64%에서 틀림.




## 다른 사람 코드 ##
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1
        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)

# 위 코드를 아래 처럼 고치면 list index out of range 에러가 난다.
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
#
# left, right = 0, 1
# cnt = 0
#
# total = sum(nums[left:right])
#
# while right <= N and left <= right:
#     if total == M:
#         cnt += 1
#         right += 1
#         total += nums[right] # 이 부분에서 # 그냥 [a : b] 는 범주를 초과해도 에러가 안 나는데, [a] 이런 방식은 초과하면 에러 난다.
#
#     elif total < M:
#         right += 1
#         total += nums[right] # 이 부분에서
#
#     else:
#         total -= nums[left]
#         left += 1
#
# print(cnt)



N, M = map(int, input().split())
nums = list(map(int, input().split()))
start = 0
end = 1
res = 0
s = nums[0]

while True:
	if s == M:
		res += 1
	if s <= M:
		if end == N: break
		s += nums[end]
		end += 1
	else:
		s -= nums[start]
		start += 1
print(res)










import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(map(int, input().split()))

start, end = 0, 0
answer = 0
value = graph[0]

while start < n and end < n:
    if value < m:
        end += 1
        if end >= n:
            break
        value += graph[end]
    elif value > m:
        value -= graph[start]
        start += 1
    else:
        answer += 1
        end += 1
        if end >= n:
            break
        value += graph[end]

print(answer)















