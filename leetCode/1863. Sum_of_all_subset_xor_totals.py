from itertools import combinations

def subsetXORSum(nums):
    result = 0

    for i in range(1, len(nums)+1):
        for s in combinations(nums,i):
            if len(s) == 1:
                result += s[0]
            else:
                tmp = 0
                for k in s:
                    tmp ^= k
                result += tmp
    return result

print(subsetXORSum([1,3]))
print(subsetXORSum([5,1,6]))


