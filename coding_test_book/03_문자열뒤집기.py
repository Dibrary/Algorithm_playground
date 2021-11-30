def test():
    nums = input() # 문자열로 들어온다.

    result = []

    start = 0

    one_cnt = 0
    zero_cnt = 0

    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            pass
        elif nums[i] != nums[i + 1]:
            result.append(nums[start:i + 1])
            start = i + 1

            # if "1" in nums[start:i+1]:   one_cnt += 1 # 리스트로 분리해서 담는 과정 대신 아예 안에 있는 값을 세려고 했었다.
            # elif "0" in nums[start:i+1]: zero_cnt += 1
            start = i + 1
    result.append(nums[start:])

    for i in range(0, len(result)):
        if "1" in result[i]:
            one_cnt += 1
        else:
            zero_cnt += 1
    print(min(one_cnt, zero_cnt))

def answer():
    data = input()
    count0, count1 = 0, 0
    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(data) - 1):
        if data[i] != data[i+1]:
            if data[i+1] == '1':
                count0 += 1
            else:
                count1 += 1
    print(min(count0, count1))


if __name__=="__main__":
    test()
    # answer()
