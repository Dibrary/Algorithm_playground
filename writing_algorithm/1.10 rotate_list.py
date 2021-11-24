'''
입력으로 정수형 배열을 준다.
각 요소를 우측으로 k만큼 이동시킨 배열을 반환해보자.
'''


def test(nums, k):
    result = [0] * len(nums)
    idx = k

    for i in nums:
        if idx > len(nums) - 1:
            idx -= len(nums)
        result[idx] = i
        idx += 1
    return result


if __name__=="__main__":
    print(test([7,5,9,4,2,6],400), test([1,2,3,4,5,6,7,8],6))
    # 이 코드 k값이 길이보다 길면 list assignment index out of range 에러남.