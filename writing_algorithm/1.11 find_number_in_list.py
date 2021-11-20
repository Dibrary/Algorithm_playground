'''
주어진 입력값은 연속적이되, 하나의 값만 없다.

없는 숫자를 찾아내자.
'''


def test(nums):
    nums.sort()

    for i in range(min(nums), len(nums)):
        if i != nums[i]:
            return i
        else:
            pass
    return -1

if __name__=="__main__":
    print(test([7,5,9,4,2,6,1,8,0]))