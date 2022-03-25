import math

sheve = [x for x in range(105000)]
sheve[1] = 0

for s in sheve[2:]:
    for k in range(2, int(math.sqrt(105000))): # 여기서 약 8초 걸려서
        if s * k < len(sheve):
            sheve[s * k] = 0

tmp = []
for x in sheve:
    if x != 0:
        tmp.append(x) # 이 값을 그냥 사용해버림. 메모리 8MB밖에 차지 안해서.

n = int(input())
print(tmp[n-1])


