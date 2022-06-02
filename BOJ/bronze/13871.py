
n,s,target = map(int, input().split())

arr = list(map(int, input().split()))

place = 1
cnt = 0

if target == 1:
    cnt += 1

for i in arr:
    if place == 1 and i == -1:
        place = n
    elif i == -1:
        place -= 1
    elif i == 1:
        place += 1
        if place > n:
            place -= n
    if place == target:
        cnt += 1

print(cnt)



