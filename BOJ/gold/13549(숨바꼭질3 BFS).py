
from collections import deque

MAX = 100000
dist = [0]*(MAX+1)
n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2): # 여기서 x*2는 1초 후에 위치로 계산이 된다. '0초 후'는 어떻게 코드로 구현이 가능할까..
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)

bfs()


