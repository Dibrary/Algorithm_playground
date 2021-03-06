'''
Find correct place index in the sorted list.

if there is no same value in the sorted list, Just return adequate place index.
'''

def test():
    print("input the int")
    nums = sorted([int(x) for x in input().split()])
    print("input the target value")
    target = int(input())

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((high + low) / 2) # I'm using binary search
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

if __name__=="__main__":
    print(test())