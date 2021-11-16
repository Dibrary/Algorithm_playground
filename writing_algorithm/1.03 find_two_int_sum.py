'''
two values in int list can make the target value as a result.
there is only one pair solution.

as a result, show the values index.
( in int list, there is never same value.)
'''

def test():
    nums = [int(x) for x in input().split()]
    target = int(input())

    for i in range(0, len(nums) - 1):
        for j in range(1, len(nums)):
            tmp = nums[i] + nums[j]
            if tmp == target:
                return i, j

if __name__=="__main__":
    print("index => ", test())