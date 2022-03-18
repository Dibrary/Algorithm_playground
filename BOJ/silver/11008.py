
n = int(input())

for _ in range(n):
    p, s = input().split()

    change_p = p.replace(s,"1")
    print(len(change_p))