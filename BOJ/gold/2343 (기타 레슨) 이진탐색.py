
'''
블루레이 갯수를 줄이려고 한다.
블루레이 크기를 최소로.

블루레이 크기가 모두 같고, 녹화 순서가 바뀌지 않아야 한다는 문장이 이진탐색을 써야 한다는 '힌트'라고 함.
강의는 순서대로 주어진다고 함 (숫자 순서가 정렬된 상태로 주어짐)

이진탐색을 2번 해야 하는게 아닌가 생각이 든다.
'''

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# def binary_check(arrs):
#     start = 0
#     end = len(arr)-1
#     min_value = 1e9
#
#     while start <= end:
#         mid = (start+end)//2
#         if abs(sum(arrs[:mid]) - sum(arrs[mid:])) <= min_value:
#             return arrs[:mid], arrs[mid:]
#         elif abs(sum(arrs[:mid]) - sum(arrs[mid:])) > min_value:
#             start = mid +1
#
# def binary_search(arr):
#     start = 0
#     end = len(arr)-1
#     min_value = 1e9
#     while start <= end:
#         mid = (start+end)//2
#         left, right_left, right_right = arr[:mid], binary_check(arr[:mid])
#         if abs(sum(left) - abs(sum(right_left)-sum(right_right))) <= min_value:
#             pass

# 코드를 작성하다가 이건 아닌거 같아서 =_=;;

# 2개의 포인터를 써버리면 연산을 100000! 갯수만큼 해야 한다.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

val = sum(arr) // 2 + 1
print(val)

min_cnt = 1e9
size = 0

for k in range(val, -1, -1):
    tmp = []
    count = 0

    for i in arr:
        if sum(tmp) + i < k:
            tmp.append(i)
        elif sum(tmp) + i >= k:  # 합했을 때 크거나 같아버리면
            tmp = []
            tmp.append(i)
            count += 1  # 블루레이 갯수 하나 증가.
    if count == m:
        print(k)
        break

# 위 코드는 시간초과 걸린다.



## 다른 사람 코드 ##

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())

lesson = list(map(int,input().split())) # 배열
l = max(lesson) # 최대값
r = sum(lesson) # 합계

ans = sys.maxsize

while l <= r: # 최대값이 합계보다 작을때만 조건문 동작.
    mid = (l+r)//2
    cnt = 0
    sum = 0
    
    for i in range(len(lesson)):
        if (sum + lesson[i]) > mid:
            cnt += 1
            sum = 0
        sum += lesson[i]
    if sum:
        cnt += 1

    if cnt > m: # 블루레이 개수가 m보다 크면 (각 크기가 작음)
        l = mid+1
    else:
        ans = min(ans, mid)
        r = mid-1
print(ans)







def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
    lesson_list = list(map(int, input().split()))  # 레슨들

    right = sum(lesson_list)   # 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기는 레슨의 합이다
    left = max(lesson_list)  # 레코드가 가질 수 있는 가장 작은 크기
    while left <= right:
        # 레코드 크기 중간값 구하기
        mid = (left + right) // 2
        cnt = add_lesson()
        if cnt <= M:  # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다.
            right = mid - 1
        elif cnt > M:  # 레코드 숫자가 더 많아지면 레코드 크기(mid)를 늘린다
            left = mid + 1

    # 답은 left 에 있다. (최소 크기)
    print(left)