
'''
버블정렬은 1회차가 끝날 때 마다 가장 큰 수가 맨 뒤로 간다.
버블 정렬의 swap이 한 번도 일어나지 않은 루프가 언제인지 알아내는 문제다.


문제에서 안쪽 루프는 1에서 n-i까지 swap을 수행해 나간다.
이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대 거리가 1이라는 의미다.

정렬 후, 각 데이터마다 정렬 전 index 값에서 정렬 후 index 값을 빼고 최대값을 찾는다.
'''
# import sys
# import copy
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# tmp = copy.deepcopy(arr)
# tmp.sort()
#
# result = 0
#
# for i in range(len(arr)):
#     if arr.index(arr[i])- tmp.index(arr[i]) > result: # 인덱스가 음수 값이면 앞으로 이동했다는 의미다.
#         result = arr.index(arr[i])- tmp.index(arr[i])
# print(result + 1)

# 위 코드 시간초과 걸린다.
# import sys
# import copy
#
# input = sys.stdin.readline
#
# n = int(input())
#
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# tmp = copy.deepcopy(arr)
# tmp.sort()
#
# result = 0
#
# for i in arr:
#     if arr.index(i) - tmp.index(i) >= result:
#         result = arr.index(i) - tmp.index(i)
# print(result+1)

# 위 코드 시간초과 걸린다.


import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

tmp = sorted(arr)

result = 0

for i in range(len(arr)):
    if arr.index(tmp[i]) - i > result: # 여기
        result = arr.index(tmp[i]) - i # 여기 index 하는 부분에서 O(n)이 걸려버려서 시간초과 됨.
print(result+1)

# 위 코드도 시간초과 걸린다.




## 다른 사람 코드 ##
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i)) # 처음에 인덱스랑 같이 값을 넣어 버린다.

sorted_arr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)






A = []
n = int(input())
for i in range(n):
    A.append((i, int(input()))) # 여기서도 미리 index를 같이 넣음.
A = sorted(A, key=lambda x: x[1])
max = 0
for i in range(n):
    if A[i][0] - i > max:
        max = A[i][0] - i
print(max+1)







n = int(input())
lst = []
copy = []
for i in range(n):
    x = int(input())
    lst.append((x, i)) # index를 같이 넣는다.

count = 0
copy = lst.copy()
lst.sort()
for i in range(n):
    x = lst[i][1] - copy[i][1]
    count = max(count,x)
print(count+1)
