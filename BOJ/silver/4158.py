import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    a = dict() # 처음에 list로 했는데, 시간이 느려서 탈락. dict로 공간을 낭비한 대신 시간을 얻음.
    for _ in range(n):
        a[int(input())] = 1

    cnt = 0
    for _ in range(m):
        value = int(input())
        if value in a:
            cnt += 1
    print(cnt)
    
