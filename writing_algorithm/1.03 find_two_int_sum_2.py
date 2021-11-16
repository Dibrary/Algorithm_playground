'''
two values in int list can make the target value as a result.
there is only one pair solution.

as a result, show the values index.
( in int list, there is never same value.)
'''

hashable_dict = {}

nums = [2,3,8,9,11,12] # sample test list
target = 17            # sample target value

def test():
    for i in range(0, len(nums)):
        tmp = target - nums[i]

        if hashable_dict.get(tmp) is not None and hashable_dict.get(tmp) != i:
            return sorted([i, hashable_dict[tmp]])

        hashable_dict[nums[i]] = i
    return [-1, 1]

if __name__=="__main__":
    print("index => ", test())