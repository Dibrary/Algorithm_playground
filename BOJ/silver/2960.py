import math

n, k = map(int, input().split())

table = [x for x in range(n+1)]
table[1] = 0

cnt = 0
result = 0
for s in table[2:]:
    cnt += 1 # 해당 값을 제거하지는 않지만, 제거했다 치고 -1을 함
    if cnt == k:
        result = table[s]
        break
    else:
        for k in range(2, n): # 문제는 이게 2부터 시작하는 것. 1로 변경해야 시작 포인트의 값도 지우는데;; 그렇게 하면 곱셈으로 지워나가지 못함.
            if s*k < len(table):
                cnt += 1
                result = table[s * k]
                print(result)
                if cnt == k:
                    break
                table[s*k] = 0
print(table)
print(result)

# 제거하는 값의 증가를 처리할 수 없음;;


