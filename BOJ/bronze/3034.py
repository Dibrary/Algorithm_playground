import math

n, w, h = map(int, input().split())
diagnal = math.sqrt(w**2 + h**2)

for _ in range(n):
    value = int(input())
    if value <= w or value <= h or value <= diagnal:
        print("DA")
    else:
        print("NE")

# 대각선 길이도 고려해야 한다.