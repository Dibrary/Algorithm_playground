
def findKthPosition(arr, k):
    cnt = 1
    for i in range(1, 100000): # 범위가 주어지지 않아서 임의로 정함.
        if i in arr:
            continue
        else:
            if cnt != k:
                cnt += 1
            else:
                return i

print(findKthPosition([2,3,4,7,11],5))

print(findKthPosition([1,2,3,4],2))