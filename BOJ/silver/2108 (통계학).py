
'''
n은 반드시 홀수개가 주어진다고 함. (중앙값 계산할 때 쓰기 용이)
'''
# import numpy as np # 백준에서 numpy 쓰면 ModuleNotFoundError 남.
#
# n = int(input())
# arr = []
# table = dict()
# max_value = -10e9
# min_value = 10e9
# total_value = 0
# cnt = 0
#
# for _ in range(n):
#     value = int(input())
#     if value > max_value:        max_value = value
#     if value < min_value:        min_value = value
#     total_value += value
#     cnt += 1
#     arr.append(value)
#     if value not in table:
#         table[value] = 1
#     else:
#         table[value] += 1
#
# print(int(round(total_value/cnt))) # 첫 번째 출력
#
# arr.sort()
# print(arr[cnt//2]) # 정렬 후 중앙값
#
# results = []
# max_cnt_value = max(table.values())
# for x in set(arr):
#     if arr.count(x) == max_cnt_value:
#         results.append(x)
# if len(results) == 1:
#     print(results[0])
# else:
#     results.sort()
#     print(results[1]) # 최빈값
#
# print(abs(max_value - min_value)) # 범위

## 위 코드는 시간초과 걸림.

# n = int(input())
# arr = []
# table = dict()
# max_value = -10e9
# min_value = 10e9
# total_value = 0
# cnt = 0
#
# for _ in range(n):
#     value = int(input())
#     if value > max_value:        max_value = value
#     if value < min_value:        min_value = value
#     total_value += value
#     cnt += 1
#     arr.append(value)
#     if value not in table:
#         table[value] = 1
#     else:
#         table[value] += 1
#
# print(int(((total_value/cnt) + 0.5))) # 첫 번째 출력
#
# arr.sort()
# print(arr[cnt//2]) # 정렬 후 중앙값
#
# results = []
# max_cnt_value = max(table.values())
# for x in set(arr):
#     if arr.count(x) == max_cnt_value:
#         results.append(x)
#         if len(results) >= 2: # 2개 까지만 알면 된다.
#             break
# if len(results) == 1:
#     print(results[0])
# else:
#     results.sort()
#     print(results[1]) # 최빈값
#
# print(abs(max_value - min_value)) # 범위

# 위 코드도 시간초과 걸림.

# n = int(input())
# arr = []
# table = dict()
# max_value = -10e9
# min_value = 10e9
# total_value = 0
# cnt = 0
#
# for _ in range(n):
#     value = int(input())
#     if value > max_value:        max_value = value
#     if value < min_value:        min_value = value
#     total_value += value
#     cnt += 1
#     arr.append(value)
#     if value not in table:
#         table[value] = 1
#     else:
#         table[value] += 1
#
# print(int(((total_value/cnt) + 0.5))) # 첫 번째 출력
#
# arr.sort()
# print(arr[cnt//2]) # 정렬 후 중앙값
#
# results = []
# max_cnt_value = max(table.values()) # 미리 담아놓은 dict에서 최대값
#
# temp = list(set(arr))
# temp.sort()
#
# for x in temp:
#     if arr.count(x) == max_cnt_value:
#         results.append(x)
#         if len(results) >= 2:
#             break
# if len(results) == 1:
#     print(results[0])
# else:
#     results.sort()
#     print(results[1]) # 최빈값
#
# print(abs(max_value - min_value)) # 범위

# 처음으로 4%까지 갔다가 시간초과 걸림.
from collections import Counter

n = int(input())
arr = []
table = dict()
max_value = -10e9
min_value = 10e9
total_value = 0
cnt = 0

for _ in range(n):
    value = int(input())
    if value > max_value:        max_value = value
    if value < min_value:        min_value = value
    total_value += value
    cnt += 1
    arr.append(value)
    if value not in table:
        table[value] = 1
    else:
        table[value] += 1

print(int(round(total_value/cnt))) # 첫 번째 출력

arr.sort()
print(arr[cnt//2]) # 정렬 후 중앙값

# 시간초과 안당하는 핵심은 이 부분에 있었다. (최빈값)
vv = sorted(Counter(arr).most_common(), key=lambda x:(-x[1], x[0])) # 최빈값.
if len(vv) == 1:
    print(vv[0][0])
else:
    if vv[0][1] == vv[1][1]:
        print(vv[1][0])
    else:
        print(vv[0][0])

print(abs(max_value - min_value)) # 범위





## 다른 사람 코드 ##

import sys
from collections import Counter

nBox = []
sum, avg, mid, mod, ran = 0, 0, 0, 0, 0


def avgFinder(nBox):
    sum, avg = 0, 0
    for i in range(0, len(nBox)):
        sum += nBox[i]
    avg = sum / len(nBox)
    return round(avg)


def midFinder(nBox):
    nBox.sort()
    mid = nBox[len(nBox) // 2]
    return mid


def modFinder(nBox):
    cntDic = Counter(nBox)
    cntTpl = cntDic.most_common()
    # print(cntTpl)
    if len(nBox) > 1:
        if cntTpl[0][1] == cntTpl[1][1]:
            mod = cntTpl[1][0]
        else:
            mod = cntTpl[0][0]
    else:
        mod = cntTpl[0][0]

    return mod


def ranFinder(nBox):
    ran = nBox[len(nBox) - 1] - nBox[0]
    return ran


n = int(sys.stdin.readline())

for i in range(0, n):
    inNum = int(sys.stdin.readline())
    nBox.append(inNum)

print(avgFinder(nBox))
print(midFinder(nBox))
print(modFinder(nBox))
print(ranFinder(nBox))













import sys

def mean(ary, N):
    m = int(0)
    for i in range(N):
        m += ary[i]
    print("%d" %round(m/N))

def middle(ary, N):
    print(ary[int(N/2)])

def mode(ary, N, max):
    data = []
    j = 0
    for i in range(8002):
        if(n[i] == max):
            data.append(int(i)-4000)
            j += 1
    if(j == 1):
        print(data[0])
    else:
        print(data[1])

def Range(ary,N):
    print(ary[N-1] - ary[0])

N = int(sys.stdin.readline())
ary = []
n = [0]*8002
max = 0
for i in range(N):
    ary.append(int(sys.stdin.readline()))
    n[ary[i] + 4000] += 1
    if(max < n[ary[i] + 4000]):
        max = n[ary[i] + 4000]
ary.sort()

mean(ary, N)
middle(ary, N)
mode(ary, N, max)
Range(ary, N)













import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()

average = round(sum(nums) / n)

median = nums[n // 2]

counts_dict = {}
for num in nums:
    if num not in counts_dict.keys():
        counts_dict[num] = 1
    else:
        counts_dict[num] += 1
counts = sorted(counts_dict.items(), key=lambda x:x[1], reverse=True) # 이건 내가 쓴 풀이랑 비슷하다.
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    mode = counts[1][0]
else:
    mode = counts[0][0]

max_min = max(nums) - min(nums)

print(average)
print(median)
print(mode)
print(max_min)
