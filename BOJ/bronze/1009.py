n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print("%d"%((a**b)%10))