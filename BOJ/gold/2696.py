import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    result = []
    for i in range(0, len(arr), 2):
        tmp = sorted(arr[:i + 1])

        if i != 0:
            result.append(tmp[int(len(tmp) / 2)])
        elif i == 0:
            result.append(tmp[0])

    print(len(result))
    if len(result) > 10:
        for k in range(0, len(result), 10):
            print(" ".join(map(str, result[k:k + 10])))
    else:
        print(" ".join(map(str, result)))

# 왜인지 런타임 에러에 걸린다.

