
nums = [4,3,2,7,8,2,3,1]

result = []
for i in nums:
    if nums.count(i) == 2 and i not in result:
        result.append(i)
result.sort()

print(result)

# 시간초과 걸리네;;




