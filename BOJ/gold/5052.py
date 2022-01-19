
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(input().strip())
    arr.sort(key=lambda x: (len(x),x)) # 길이, 값으로 정렬 (값정렬은 필요 없어보이는듯)

    flag = 0
    for s in range(0, len(arr)-1):
        tmp = arr[s]
        length = len(tmp)
        for k in range(s+1, len(arr)):
            if flag == 1:
                break
            else:
                if tmp == arr[k][:length]:
                    flag = 1
                    break
                else:
                    continue
    if flag == 1:
        print("NO")
    else:
        print("YES")
# 위 방법은 전부 확인하는 것으로, 시간초과 난다.









