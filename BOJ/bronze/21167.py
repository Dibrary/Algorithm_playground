import math

try:
    while True:
        r, s = input().split()
        r = int(r)
        s = float(s)
        v = math.sqrt((r*(s+0.16))/0.067)
        print(int(round(v, 1)))
except:
    pass

# 틀림
