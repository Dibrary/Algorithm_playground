
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if len(arr) == 1:
    print(arr[0])
elif len(arr) >= k:
    print(arr[-k])



