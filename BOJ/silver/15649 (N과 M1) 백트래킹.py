n, m = list(map(int, input().split()))

visited = [False] * (n + 1)
tmp = []

def backtrack(n, deep, tmp, visited):
    if deep == m:
        out = ""
        for k in tmp:
            out += str(k) + " "
        print(out[:-1])
        return

    for i in range(1, n + 1):
        if not visited[i]:
            tmp.append(i)
            visited[i] = True
            backtrack(n, deep + 1, tmp, visited)
            tmp.pop()
            visited[i] = False

backtrack(n, 0, tmp, visited)


## 다른 사람 코드 ##

n, m = map(int, input().split(' '))

res = []

def dfs(depth) :
    if depth == m:
        print(' '.join(map(str,res)))
        return
    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            dfs(depth + 1)
            res.pop()

dfs(0)














def dfs(cnt):
    if cnt == M:
        print(*num)
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        num.append(i + 1)
        dfs(cnt + 1)
        num.pop()
        used[i] = 0


N, M = map(int, input().split())

used = [0 for _ in range(N)]  # 숫자 사용 확인
num = []  # 수열

dfs(0)

