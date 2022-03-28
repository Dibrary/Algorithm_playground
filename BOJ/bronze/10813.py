
n, m = map(int, input().split())

balls = [x for x in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    balls[a], balls[b] = balls[b], balls[a]

balls.pop(0)
print(" ".join(map(str, balls)))

