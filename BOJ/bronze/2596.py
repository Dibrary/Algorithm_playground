
table = {"000000":"A","001111":"B","010011":"C","011100":"D","100110":"E","101001":"F","110101":"G","111010":"H"}

n = int(input())
arr = input()
tmp = []
for i in range(0, len(arr), 6):
    tmp.append(arr[i:i+6])

result = ""
cnt = 0
for k in tmp:
    if k in table:
        result += table[k]
        cnt += 1
    else:
        # 여기서 차이를 확인해야 하는데;; 그러면 코드가 너무 복잡.
        pass
