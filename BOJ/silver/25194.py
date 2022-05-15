import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

days = 4 # 처음에는 4로 시작하고 그 뒤에 7을 계속 더해서 비교해야 한다.
sum_days = 0
flag = 0

if days in arr:
    print("YES")
else:
    while arr:
        value = arr.pop(0)
        sum_days += value
        if sum_days < days:
            continue
        elif sum_days == days:
            print("YES")
            flag = 1
            break
        elif sum_days > days:
            days += 7

    if flag == 0:
        print("NO")

# 2% 에서 바로 틀림.





