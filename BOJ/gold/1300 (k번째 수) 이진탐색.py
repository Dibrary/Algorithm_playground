
'''
문제의 핵심은 이 문장이다
"이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자."

k범위가 min(10^9, N^2) 라서 O(N^2) 알고리즘은 사용 못 한다.

중앙값보다 작거나 같은 수의 갯수는 중앙값을 N(열 index)으로 나눈 값이다.
'''

# n = int(input())
# k = int(input())

# tmp = [[] for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         tmp[i].append(i*j) # 배열은 이런 꼴로 만들어진다.

# 규칙을 찾아내면 배열 자체를 만들 필요가 없다.


n = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    mid = int((start + end)/2) # mid는 중앙값이다.
    cnt = 0

    for i in range(1, n+1):
        cnt += min(int(mid/i), n)

    if cnt < k:
        start = mid+1
    else: # k보다 cnt가 크거나 같으면
        ans = mid
        end = mid-1

print(ans)



## 다른 사람 코드 ##


N, K = int(input()), int(input())
s, e = 1, K

while s <= e:
    mid = (s + e) // 2

    a = 0
    for i in range(1, N + 1):
        a += min(mid // i, N)

    if K <= a:
        res = mid
        e = mid - 1
    else:
        s = mid + 1
print(res)





N = int(input())
K = int(input())
end = min(int(1e9), N ** 2)
start = 1

def nums_before(num):
    total = 0
    for i in range(1, N+1):
        total += min(num // i, N)
    return total

while start <= end:
    mid = (start + end) // 2
    if nums_before(mid) >= K:
        end = mid - 1
    else:
        start = mid + 1

print(start)