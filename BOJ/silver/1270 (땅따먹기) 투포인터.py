
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# peoples = 0
# armys = None
#
#
# for i in range(n):
#     peoples, *armys = map(int, input().split())
#     tmp = set(armys)
#     divide = len(armys)/2
#
#     flag = 0
#     for i in tmp:
#         if armys.count(i) > divide:
#             print(i)
#             flag = 1
#             break
#     if flag == 0:
#         print("SKJKGW")

# 위 코드는 시간초과 걸린다.

import heapq

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    peoples, *armys = map(int, input().split())

    key = set(armys)
    q = []
    divide = len(armys) / 2

    for i in key:
        heapq.heappush(q, (armys.count(i) * (-1), i)) # 아무래도 이 count에서 계속 O(n) 잡아먹어서 그런듯

    value, solder = heapq.heappop(q)

    if value * (-1) > divide:
        print(solder)
    else:
        print("SYJKGW")
# 위 코드도 9%까지는 진행 되었으나, 시간초과 걸린다.

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    land = list(map(int, input().split()))[1:]
    land.sort()

    left = right = 0
    answer = []

    while right < len(land):
        if land[left] == land[right]: # 같으면 무조건 right만 진행시킴.
            right += 1
        else: # 다르면
            answer.append((right - left, land[left])) # right-left로 갯수를 센다.
            left = right
    answer.append((right - left, land[left]))
    answer.sort() # 갯수가지고 정렬됨.

    cnt, army = answer[-1]  # 갯수가 제일 큰 값이
    if cnt > len(land) / 2:  # 절반값보다 이상이면
        print(army)  # 출력
    else:
        print("SYJKGW")


## 다른 사람 코드 ##
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    land = list(map(int, input().split()))
    land.sort()

    left = right = 0
    answer = []
    while right < len(land):
        if land[left] == land[right]:
            right += 1
        else:
            answer.append((right-left, land[left]))
            left = right
    answer.append((right - left, land[left]))
    answer.sort()

    cnt, army = answer[-1]
    if cnt >= len(land)/2:
        print(army)
    else:
        print("SYJKGW")












import sys
n = int(sys.stdin.readline())
for _ in range(n) :
    L = list(map(int, sys.stdin.readline().split()))
    d = {}
    maxi = 0
    for i in range(1,len(L)):
        if L[i] in d.keys() :
            d[L[i]] += 1
            if d[L[i]] > maxi :
                maxi = d[L[i]]
        else :
            d[L[i]] = 1
    if list(d.values()).count(maxi) >= 2 or maxi <= L[0]//2 :
        print('SYJKGW')
    else :
        for i in d.keys() :
            if d[i] == maxi:
                print(i)
                break










import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    war = list(map(int, input().rstrip().split()))
    total_soldier = war[0]
    soldier_dic = {}

    for soldier_num in war[1:]:
        if soldier_num not in soldier_dic:
            soldier_dic[soldier_num] = 1
        else:
            soldier_dic[soldier_num] += 1
    if max(soldier_dic.values()) <= total_soldier//2:
        print('SYJKGW')
    else:
        print(max(soldier_dic, key=soldier_dic.get))