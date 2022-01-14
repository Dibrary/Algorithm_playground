n, k = map(int, input().split())
arr = [int(x) for x in input().split(",")]
tmp = []
for _ in range(k):
    for s in range(1,len(arr)):
        tmp.append(arr[s]-arr[s-1])
    arr = tmp
print(",".join(map(str,tmp)))
# 위 코드 처럼 작성하면 메모리 초과가 된다.

n, k = map(int, input().split())
arr = [int(x) for x in input().split(",")]
for _ in range(k):
    for s in range(1,len(arr)):
        arr[s-1] = (arr[s]-arr[s-1])
    arr.pop()
print(",".join(map(str,arr)))