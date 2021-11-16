'''
Correct that sorted list in place.

Return the new list length which components is no overlaped.
'''

def test():
    nums = [int(x) for x in input().split()]

    if nums == []:
        return []

    start_idx = 0
    length = 0

    for i in range(1, len(nums)):
        if nums[start_idx] == nums[i]:
            pass
        else:  # if different values.
            nums[start_idx + 1] = nums[i]
            start_idx += 1
            length += 1
    return nums, length

if __name__=="__main__":
    print(test())