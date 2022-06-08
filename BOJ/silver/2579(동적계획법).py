
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




