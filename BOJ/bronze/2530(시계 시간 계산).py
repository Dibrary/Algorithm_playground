# a, b, c = map(int, input().split())
#
# during = int(input()) # 이 값이 초 단위다.
#
# second = during%60
# minute = during//60
#
# hour = 0
# if minute >= 60:
#     hour = minute//60
#     minute = minute-(hour*60)
#
# a += hour
# b += minute
# c += second
#
# if c >= 60:
#     c -= 60
#     b += 1
# if b >= 60:
#     b -= 60
#     a += 1
# if a >= 24:
#     a -= 24
#
# print(a, b, c)

# 틀렸대

a, b, c = map(int, input().split())

during = int(input()) # 이 값이 초 단위다.

second = during%60
minute = during//60

hour = 0
if minute >= 60:
    hour = minute//60
    minute = minute-(hour*60)

a += hour
b += minute
c += second

if c >= 60:
    b += c // 60
    c = c%60

if b >= 60:
    a += b // 60
    b = b%60

if a >= 24:
    a = a%24

# print(hour, minute, second)
print(a, b, c)

# 시간 단위가 넘으면 무조건 += 을 하는게 아니라 어떤 결과가 나올지 생각하고 연산자 써야 함.

