
# 아이디어가 필요하다.
# 끝나는 시간이 가장 시작점과 가까운 것을 계속 택하면 된다.

# n = int(input())
#
# keys = dict()
# table = []
#
# start_time = 0
# start_end_std = 2**31-1
# end_point = 0
#
#
# for _ in range(n):
#     start, end = map(int, input().split())
#     table.append([start, end])
#     if end > end_point:
#         end_point = end
#
#     if end < start_end_std:
#         start_end_std = end
#         start_time = [start, end]
#
#     if start not in keys:
#         keys[start] = [[start, end]]
#     else:
#         keys[start].append([start, end])
#
# for s in keys:
#     keys[s].sort(key = lambda x:x[1])
#
# cnt = 1
# result = []
#
# while start_end_std <= end_point:
#     if start_end_std not in keys: # 없으면
#         start_end_std += 1
#         continue
#     else: # 있으면
#         s, e = keys[start_end_std][0] # 무조건 첫 번째만.
#         result.append([s,e])
#         start_end_std = e
#         cnt += 1
#
# print(cnt)

# 5%에서 틀림


'''
반례가 있다.
11
1 2
2 4
3 3
4 17
5 7
6 9
7 15
8 10
10 12
11 12
13 14
일케 하면

[1,2],[3,3],[5,7],[8,10],[11,12],[13,14] 이래서 6가 나와야 가장 갯수가 많은데
끝만 확인하니 3이 나온다.
'''

# 한 방향만 고려하면 안 된다.
# 인터넷 검색을 해 보니 "빨리 끝나는 회의 순서대로 정렬을 해야 한다." 라고 함.

# n = int(input())
#
# table = []
# for _ in range(n):
#     table.append(list(map(int, input().split())))
#
# table.sort(key=lambda x:(x[1],x[0]))
#
# cnt = 0
# # 여기서 while문 쓰려면 어떤 조건에 멈추게 할 지 정해야 함.


import sys
input = sys.stdin.readline

n = int(input())

time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time: # 시작시간이 end_time보다 크거나 같으면 
        cnt += 1
        end_time = time[i][1] # 해당 스케쥴의 끝시간을 end_time으로 갱신

print(cnt)

# 생각보다 진행 시간은 빠르다.


