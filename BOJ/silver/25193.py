
n = int(input())
s = input()

tmp = []
start_idx = 0

max_length = 0
max_value = ""

for idx, i in enumerate(s):
    if i != "C":
        tmp.append(s[start_idx:start_idx + idx+1])
        start_idx = start_idx + idx+1

print(tmp)
# 위 코드는 CCCC 인 경우 tmp = [] 됨.

# 오 이거 생각보다 어렵다.
'''
ACCCC에서 CCACC 로 만들어야 함.

max값의 절반으로 줄여야 함.
'''



