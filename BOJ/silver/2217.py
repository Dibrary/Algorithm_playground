import sys
# 이 문제의 함정은 "모든 로프를 안 쓸 수도 있다" 는 문구다.

n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)# 큰 값이 앞으로
max_weight = 0
for i in range(0, len(ropes)):
    for j in range(i+1, len(ropes)+1):
        tmp = min(ropes[i:j])*len((ropes[i:j]))
        if tmp < max_weight:
            continue
        else:
            max_weight = tmp
print("%d"%(max_weight))


