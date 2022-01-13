
import sys

n, m = list(map(int, sys.stdin.readline().split()))
strings = []

for _ in range(m):
    six, one = list(map(int, sys.stdin.readline().split()))
    strings.append((six, one))
strings.sort(key=lambda x:x[0])

value1 = n/6
value2 = n%6
value3 = value1+1

tmp3 = (value3*strings[0][0])
tmp1 = (value1*strings[0][0])

strings.sort(key=lambda x:x[1])
tmp2 = (value2*strings[0][1])

print(tmp3, tmp1, tmp2)
if tmp3 < tmp1+tmp2:
    print(tmp3)
else:
    print(tmp1+tmp2)

# 6 1
# 7 1 이게 반례다. (정답은 6이 나와야 됨)



