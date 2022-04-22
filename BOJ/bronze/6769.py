
string = input()

start_idx = 0

tmp = []

for idx, i in enumerate(s):
    if i.isascii() and i.isdigit() == False:
        tmp.append(s[start_idx:idx+1])
        start_idx = idx+1

table = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

result = 0

# 이제 계산하는 것은 쉬운데, + - 규칙이 명확하지 않다.


