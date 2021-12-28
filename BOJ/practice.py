import sys

def searching(DDUK, target, start, end):
    if start > end:
        return False

    mid = (start + end)//2

    tmp = 0
    for i in DDUK:
        if i < mid:
            continue
        else:
            tmp += (i - mid)
    print(tmp)

    if tmp == target:
        return mid
    elif tmp < target:
        return searching(DDUK, target, start, mid-1)
    else:
        return searching(DDUK, target, mid+1, end)


n, target = list(map(int, input().split()))
DDUK = list(map(int, sys.stdin.readline().split()))

min_value, max_value = min(DDUK), max(DDUK)
print(searching(DDUK, target, min_value, max_value))

