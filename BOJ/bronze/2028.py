
n = int(input())
for _ in range(n):
    value = int(input())
    result = str(value**2)

    if result[-len(str(value)):] == str(value):
        print("YES")
    else:
        print("NO")




