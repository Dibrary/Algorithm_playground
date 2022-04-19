
n = int(input())

for _ in range(n):
    a, b = input().split()
    cnt = 0
    for i in a:
        if i in b:
            cnt += 1
        b = b.replace(i, "")
    if b == "" and cnt == len(a):
        print("YES")
    else:
        print("NO")




