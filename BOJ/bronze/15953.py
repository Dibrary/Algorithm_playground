
first = [0]+[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6
second = [0]+[512]+[256]*2+[128]*4+[64]*8+[32]*16

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    if a >= len(first): a = 0
    else:              a = first[a]

    if b >= len(second):b = 0
    else:              b = second[b]

    print("%d"%((a+b)*10000))




