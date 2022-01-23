
def maxAscendingSum(nums):
    table = []
    start = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            continue
        else:
            table.append(nums[start:i])
            start = i
    table.append(nums[start:])

    result = 0
    for i in table:
        tmp = sum(i)
        if tmp >= result:
            result = tmp
    return result