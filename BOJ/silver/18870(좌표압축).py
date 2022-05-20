import copy

n = int(input())
arr = list(map(int, input().split()))
tmp = copy.deepcopy(arr) # 순서 맞추기 용도

arr = list(set(arr))
arr.sort()

table = dict()
for idx, k in enumerate(arr):
    if k not in table:
        table[k] = idx

print(" ".join(map(str, [table[x] for x in tmp])))

# 이 코드는 채점이 너무 오래 걸림.

#### 남의 코드 #####


N = int(input())
arr = list(map(int, input().split()))
order = {}
for i, k in enumerate(sorted(list(set(arr)))):
    order[k] = str(i)
print(" ".join(list(map(lambda x: order[x], arr))))


### 다른 코드 ###
import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int,input().split()))
result = sorted(list(set(l)))
dic = {result[i] : i for i in range(len(result))}
for i in range(n):
    print(dic[l[i]],end=' ')






