# 처음에 먼저 모든 숫자를 이어서 만든 변수의 크기를 sys.getsizeof로 측정함

tmp = [x for x in range(1, 100001)]
table = ""
for i in tmp:
    table += str(i)

n = input()
length = len(n)

result = 0
for i in range(0, len(table)-1):
    if table[i:i+length] == n:
        result = i+1
        break
print(result)

