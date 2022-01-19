
n = int(input())

arr = []
for _ in range(n):
    nation, student, score = map(int, input().split())
    arr.append((nation, student, score))
arr.sort(key=lambda x:(x[2]), reverse=True)

table = dict()
cnt = 0
for i in arr:
    if i[0] not in table or table[i[0]] < 2:
        print("%d %d"%(i[0],i[1]))
        cnt += 1
    else:
        continue
    if cnt == 3:
        break
    if i[0] not in table:table[i[0]] = 1
    else:                table[i[0]] += 1

# 위 코드에서 중요한 포인트는, table에 넣은 횟수를 몇으로 거르느냐. 그리고 정렬조건.