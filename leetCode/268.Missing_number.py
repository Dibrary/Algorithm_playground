import copy

def test(nums):
    if max(nums) == len(nums):
        nums.sort()
        for i in range(0, len(nums)):
            if i+1 == nums[i]:
                return i+1
    else:
        return max(nums)+1
