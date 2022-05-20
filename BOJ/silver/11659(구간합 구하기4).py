# import sys
# n, m = list(map(int, sys.stdin.readline().split()))
# arr = list(map(int, sys.stdin.readline().split()))
# for _ in range(m):
#     i, j = list(map(int, sys.stdin.readline().split()))
#     print("%d"%(sum(arr[i-1:j])))

# 시간초과 걸림

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# for _ in range(n):
#     start, end = map(int, input().split())
#     print(sum(arr[start-1:end]))

# 이 코드도 시간초과 걸린다.



# 전체 누적합 배열을 하나만 만들어 놓으면 구간합을 쉽게 구할 수 있다는데, 누적합에서 빼도 구간의 합이 나오지 않음;

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
for i in (arr):
    sum_arr.append(sum_arr[-1]+i)

for _ in range(m):
    start, end = map(int, input().split())
    print(sum_arr[end]-sum_arr[start-1])

# 코드를 이렇게 쓰니 확실히 채점 속도가 빠르다.

