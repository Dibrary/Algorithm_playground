
a = list(map(int, input().split()))
A = list(map(int, input().split()))

result = 0
for i in range(0, len(a)):
    tmp = A[i] - a[i]
    if tmp > 0:
        result += tmp

print(result)

