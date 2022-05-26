
arr = list(map(int, input().split()))

first = []

p = 0

for i in range(len(arr)+1):
    if len(first) == p and i == p:
        first.append(0)
    elif len(first) == p+1 and i == p+1:
        first.append(arr[i-1])
    else:
        first.append(first[-1]+arr[i-1])

# 이렇게는 나오는데 이 방법으로는 2번째 줄 까지만 가능하고 3번째 줄 부터 첫 번째 값 설정 못함.




