n, l, h = map(int, input().split())
values = list(map(int, input().split()))

values.sort()

total_value = 0
cnt = 0
if l == 0 and h != 0:
    total_value = sum(values[:-h])
    cnt = len(values[:-h])
elif l != 0 and h == 0:
    total_value = sum(values[l:])
    cnt = len(values[l:])
elif l == 0 and h == 0:
    total_value = sum(values)
    cnt = len(values)
else:
    total_value = sum(values[l:-h])
    cnt = len(values[l:-h])

print(total_value/cnt)