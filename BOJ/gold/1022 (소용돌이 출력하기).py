
r1, c1, r2, c2 = map(int, input().split())

length = max(abs(r1*2)+1, abs(r2*2)+1)
height = max(abs(c1*2)+1, abs(c2*2)+1)

max_length= max(length, height)
arr = [[0 for _ in range(max_length)] for _ in range(max_length)]

nx = len(arr)//2
ny = len(arr)//2
arr[ny][nx] = 1 # 정 중앙에 1 넣음.

start_value = 2


for k in range(1, max_length):
    if k%2 != 0:
        for m in range(k):
            nx += 1
            arr[ny][nx] = start_value
            start_value += 1
        for s in range(k):
            ny -= 1
            arr[ny][nx] = start_value
            start_value += 1
    else:
        for m in range(k):
            nx -= 1
            arr[ny][nx] = start_value
            start_value += 1
        for s in range(k):
            ny += 1
            arr[ny][nx] = start_value
            start_value += 1


# 위 코드까지만 하면 맨 아래쪽 값이 빈다.
for k in range(ny):
    nx += 1
    arr[ny][nx] = start_value
    start_value += 1

# 여기까지 arr의 값이 다 찬다.

center = len(arr)//2

r1 = center+r1
c1 = center+c1

r2 = center+r2
c2 = center+c2

for i in range(r1, r2+1):
    tmp = []
    for j in range(c1, c2+1):
        tmp.append(arr[i][j])
    print(" ".join(map(str, tmp)))

# 위 코드는 -2,2,0,3 에서 에러남.
'''
length = max(abs(r1*2)+1, abs(r2*2)+1)
height = max(abs(c1*2)+1, abs(c2*2)+1)
이 부분을 max로 수정함. 

원래는 
length = abs(r1*2)+1
height = abs(c1*2)+1
이었음.
'''

# 위 코드로 제출하면 메모리 초과가 난다. 5000 범주로 넣어버리면 시간이 너무 오래 걸림;








