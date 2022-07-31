
'''
투 포인터는 2개의 포인터를 써서 알고리즘 시간복잡도를 최적화 한다.

O(nlogn)으로 풀려고 할 때 제한시간을 초과하면 O(n)으로 풀어야 하는데, 이런 경우 자주 사용하는 것이 투 포인터 방법이다.

이 문제는 메모리 제한이 32MB로 작다.
'''
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# cnt = 0
#
# for i in range(1, n+1):
#     for j in range(i+1, n+2):
#         if sum([x for x in range(i, j)]) == n:
#             cnt += 1
# print(cnt)

# 메모리 초과 뜸


## 책 풀이 ##
import sys
input = sys.stdin.readline

n = int(input())
count = 1
start_idx = 1
end_idx = 1
total = 1

while end_idx != n: # 사실상 반복문이 하나 뿐이므로 O(n)이 된다.
    if total == n:
        count += 1
        end_idx += 1
        total = total + end_idx
    elif total > n:
        total = total - start_idx # start_idx값을 빼고
        start_idx += 1 # start_idx를 하나 높인다.

    else: # 위 두 경우에 해당하지 않는다면,
        end_idx += 1
        total = total + end_idx

print(count)







## 다른 사람 코드 ##
n = int(input())
c = l = r = S = 1

while l*2<=n:
    if S>=n:
        c += S == n
        l = r = S = l+1
    r+=1;S+=r
print(c)










import sys
N = int(sys.stdin.readline())
cnt = 0
i = 1
k = 1
while k <= N :
    if (N - k) % i == 0 :
        cnt += 1
    i += 1
    k = i * (i + 1)//2
print(cnt)