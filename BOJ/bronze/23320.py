
n = int(input())

a = list(map(int, input().split()))

x, y = map(int, input().split())

value = len([k for k in a if k >= y])

print(int(n*(x/100)), value)

# 위 코드 틀림

