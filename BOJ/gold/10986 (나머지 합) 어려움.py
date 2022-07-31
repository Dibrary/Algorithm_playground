
'''
구간합 배열을 이용하면 용이.
'''

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = [0]+list(map(int, input().split()))
# add_arr = [0 for _ in range(n+1)]
# for i in range(1, n+1):
#     add_arr[i] = arr[i]+add_arr[i-1]
#
# tmp = [0 for _ in range(n+1)]
# for j in range(1, n+1):
#     tmp[j] = add_arr[j]%m
#
# zero_cnt = tmp.count(0)-1
# one_cnt = tmp.count(1)
#
# from itertools import combinations
# total = zero_cnt
# for i in range(one_cnt, zero_cnt+1):
#     total += len(list(combinations([x for x in range(i)], one_cnt)))
# print(total)

# 위 코드 틀림


'''
(A+B)%C는 (A%C)+(B%C)와 같다.
특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일하다.

S[i]%M과 S[j]%M의 값이 같으면 (S[i]-S[j])%M = 0 이 된다.

'''

n, m = map(int, input().split())
C = [0 for _ in range(m+1)]
S = list(map(int, input().split()))

answer = 0

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1
print(C, S)

for i in range(m):
    if C[i]>1:
        answer = answer +(C[i]*(C[i]-1)/2)

print(answer)











