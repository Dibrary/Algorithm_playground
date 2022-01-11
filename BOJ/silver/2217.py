import sys
# 이 문제의 함정은 "모든 로프를 안 쓸 수도 있다" 는 문구다.

n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)# 큰 값이 앞으로
max_weight = 0
for i in range(1, len(ropes)+1):
    tmp = ropes[i-1] # 핵심은 굳이 min값을 구하는데 [:i]로 범위 꺼낸뒤에 min(ropes[:i]) 이렇게 할 필요 없다는 것. (시간초과됨)
    if max_weight <= tmp*i:
        max_weight = tmp*i
    else: # 이거 넣으면 틀림.
        break
print("%d"%(max_weight))


