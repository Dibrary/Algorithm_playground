
n, k = map(int, input().split())

table = []
for i in range(1, k+1):
    table.append(int(str(n*i)[::-1])) # 한 번에 문자열로 바꿔서 위치를 바꿈.

print(max(table))  # 최대값 출력
