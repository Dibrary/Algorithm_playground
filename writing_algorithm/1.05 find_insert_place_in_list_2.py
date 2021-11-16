'''
Find correct place index in the sorted list.

if there is no same value in the sorted list, Just return adequate place index.
'''

def test():
    print("input the int")
    nums = sorted([int(x) for x in input().split()])
    print("input the target value")
    target = int(input())

    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i
    return -1

if __name__=="__main__":
    print(test())