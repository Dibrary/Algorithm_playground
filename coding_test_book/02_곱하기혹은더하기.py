
def test():
    nums = [int(x) for x in list(input())] # 입력 한번에 받자마자, 각 값으로 잘라버림.

    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i]* nums[i-1] == 0:
            result += nums[i]
        else:
            result *= nums[i]
    print(result)

def answer():
    data = input()
    result = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)


def answer():
    return None


if __name__=="__main__":
    test()
    # answer()