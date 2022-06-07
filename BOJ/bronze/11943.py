#
# a, b = list(map(int, input().split()))
# c, d = list(map(int, input().split()))
# mini_value = min(a, b, c, d)
#
# result = mini_value
# if mini_value == a:  result += d
# elif mini_value == b:result += c
# elif mini_value == c:result += b
# else:                result += a
# print(result)

# 틀림

a, b = map(int, input().split())
c, d = map(int, input().split())

print(min(a+b, c+d))

# 11% 에서 틀린다.

# 덧셈을 잘못했다.

print(min(a+d, c+b))

