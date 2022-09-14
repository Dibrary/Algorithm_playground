
# import sys
# input = sys.stdin.readline
#
# a, b, c = map(int, input().split())
# print((a**b)%c)

## 당연하게도 위 코드는 시간초과 걸린다.


a, b, c = map(int, input().split())

first = b//3
second = b%3

result = 1
for x in range(first):
    result *= a**3

print((result*(a**second))%c)

# 이렇게 하니 3%까지는 진행되고 시간초과 걸린다.













