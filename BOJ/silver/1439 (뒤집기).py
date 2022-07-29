# s = input()
# zero_cnt = 0
# one_cnt = 0
# for i in range(0, len(s)-1):
#     print(s[i], s[i+1], "값")
#     if s[i] != s[i+1] and s[i] == 1:
#         one_cnt += 1
#     elif s[i] != s[i+1] and s[i] == 0:
#         zero_cnt += 1
# print(zero_cnt, one_cnt)

# import sys
# s = sys.stdin.readline() # 이 코드도 17%정도에서 틀림.
#
# if "0" not in s: # 아예 처음부터 1만 있으면 바꿀 필요가 없다.
#     print(0)
# else:
#     if s[-1] =="0": s+= "1"
#     else:           s+= "0"
#     start = 0
#     one_cnt, zero_cnt = 0, 0
#
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:
#             if "1" in s[start:i]:
#                 one_cnt += 1
#             else:
#                 zero_cnt += 1
#             start = i
#     print(one_cnt, zero_cnt)
#     if min(one_cnt, zero_cnt) == 0:
#         print(1)
#     else:
#         print("%d"%(min(one_cnt, zero_cnt)))

import sys

s = sys.stdin.readline()

if "1" not in s:
    print(0)
elif "0" not in s:
    print(0)
else:
    if s[-1] == "0": s += "0"
    else:            s += "1"

    zero_cnt, one_cnt = 0,0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            if s[i] == "1":   one_cnt += 1
            elif s[i] == "0": zero_cnt += 1 # 이 부분 그냥 else로 빼면 에러남.
    print("%d"%(min(one_cnt, zero_cnt)))


## 다른 사람 코드 ##

values = input()

prev = int(values[0])
cnt = [0, 0]
cnt[prev] += 1
for v in values[1:]:
    v = int(v)
    if prev != v:
        cnt[v] += 1  ## end
    prev = v

print(min(cnt[0], cnt[1]))








import sys
input = sys.stdin.readline

s = input().strip()
split_0 = s.split("0")
split_1 = s.split("1")
result = min(len(split_0) - split_0.count(''), len(split_1) - split_1.count(''))
print(result)