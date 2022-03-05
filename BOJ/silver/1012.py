import sys
sys.setrecursionlimit(10**6) # 재귀 횟수 1000번을 넘게 실행할 수 있게 해 주는 것.

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    cabbage_map = [[0 for _ in range(m)] for _ in range(n)]
    # 처음에 여길 map으로 변수 이름 했다가 아래에서 계속 에러남.

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage_map[y][x] = 1


    def dfs(y, x):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if cabbage_map[y][x] == 1:
            cabbage_map[y][x] = 0
            dfs(y, x-1)
            dfs(y-1,x)
            dfs(y,x+1)
            dfs(y+1,x)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)

# 결과는 맞는데  RecursionError 걸린다.



