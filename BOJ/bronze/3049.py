
n = int(input())
if n == 3:
    print(0)
elif n == 4:
    print(1)
else:
    result = int((n*(n-1)*(n-2)*(n-3))/24)
    print(result)

# 이건 nC4 라는 공식이 존재한다.


