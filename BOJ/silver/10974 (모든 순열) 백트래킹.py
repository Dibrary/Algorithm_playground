from itertools import permutations

n = int(input())

for x in permutations([x+1 for x in range(n)], n):
    print(" ".join(map(str, x)))

## 백트래킹으로도 풀어보자.

n = int(input())
values = [i for i in range(1, n+1)]
result = []

def recursive(level):
    if level == n:
        print(*result)
        return

    for i in range(n):
        if values[i] not in result:
            result.append(values[i])
            recursive(level+1)
            result.pop()

recursive(0)



