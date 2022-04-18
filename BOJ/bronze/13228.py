n = int(input())
for _ in range(n):
    distance = 0

    x1, y1, f1, x2, y2, f2 = map(int, input().split())
    distance += f1
    distance += (abs(x1 - x2) + abs(y1 - y2))
    distance += f2
    print(distance)
