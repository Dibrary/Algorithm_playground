
n = int(input())

stairs = []
for _ in range(n):
    # stairs.insert(0,int(input()))
    stairs.append(int(input()))

result = stairs[0]
idx = 0

while True:
    if (idx+1 > len(stairs)) or (idx+2 > len(stairs)):
        break
    else:
        if stairs[idx+1]> stairs[idx +2]:
            result += stairs[idx+1]
            idx += 1
        elif stairs[ idx+1] < stairs[idx +2]:
            result += stairs[idx+2]
            idx += 2

# 위 코드 반례 10,20,15,25,39,20



# arr = [10, 20, 15, 25, 10, 20]
# tmp = [arr[0]] + [0 for _ in range(len(arr)-1)]
# for x in range(1, len(arr)):
#     if x-1 < 0:
#         a = arr[x]+0
#     else:
#         a = arr[x]+tmp[x-1]
#     if x-2 < 0:
#         b = arr[x]+0
#     else:
#         b = arr[x]+tmp[x-2]
#     print(a, b)
#     tmp[x] = (max(a, b))

# 약간 이런식으로 하는 것 같은데... 문제는 위 처럼 해 버리면 연속 3칸 진행 하는 것도 되는 꼴임.

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

tmp = [(True, arr[0])] + [0 for _ in range(len(arr) - 1)]
for x in range(1, len(arr)):
    if x - 1 < 0:
        a = arr[x] + 0
    else:
        if tmp[x - 1][0] == False:
            a = arr[x]
        else:
            a = arr[x] + tmp[x - 1][1]
    if x - 2 < 0:
        b = arr[x] + 0
    else:
        b = arr[x] + tmp[x - 2][1]
    tmp[x] = (False, a) if max(a, b) == a else (True, b)
print(tmp[-1][1])

## 위 코드 틀림


