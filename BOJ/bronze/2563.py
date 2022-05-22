
n = int(input())

tmp = set() # 겹치는 부분만 제외하고 각 점의 갯수를 합하면 해당 면적이 되는 것을 파악함.

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            tmp.add((i, j))

print(len(tmp))



