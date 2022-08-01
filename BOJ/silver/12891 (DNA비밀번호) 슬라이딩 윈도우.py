
'''
P와 S의 길이가 매우 크므로 O(n)의 시간복잡도 알고리즘으로 문제를 풀어야 한다.

'''
# import sys
# input = sys.stdin.readline
#
# S, P = map(int, input().split())
# string = input()
# a, c, g, t = map(int, input().split())
#
# cnt = 0
# for i in range(len(string)-P+1):
#     target = string[i:i+P]
#     if target.count("A") >= a and target.count("C") >= c and target.count("G") >= g and target.count("T") >= t:
#         cnt += 1
# print(cnt)

# 이렇게 하면 시간초과 걸린다.

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
string = input().rstrip()

a, c, g, t = map(int, input().split())

result = 0

start = string[:P]

tmp = {"A":0, "C":0, "G":0, "T":0}
for i in start:
    tmp[i] += 1

cnt = 0
if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
    cnt += 1

start_idx = 0
end_idx = start_idx + P

for i in range(len(string)-P):
    tmp[string[start_idx+i]] -= 1
    tmp[string[end_idx+i]] += 1 # 슬라이딩 윈도우 방식으로 dict값을 수정해 나간다.
    if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t: # 갯수가 해당되면 cnt를 증가.
        cnt += 1
print(cnt)

# 사전으로 바꾸니까 시간초과 해결 됨.


# 다른 사람 풀이도 대부분 dict를 사용함.


