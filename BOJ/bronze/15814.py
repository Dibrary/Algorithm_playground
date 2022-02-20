
s = input()
n = int(input())

s = list(s)
for _ in range(n):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]

print("".join(map(str, s)))

