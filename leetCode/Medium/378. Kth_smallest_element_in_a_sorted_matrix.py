
def kthSmallest(matrix, k):
    tmp = []
    for i in matrix:
        tmp += i
    tmp.sort()
    return tmp[k-1]

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))

print(kthSmallest([[-5]],1))

print(kthSmallest([[1,2],[1,3]],2))


# sort를 넣어 줘야 함.
