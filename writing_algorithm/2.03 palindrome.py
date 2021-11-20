'''

주어진 문자열의 좌우 대칭값이 맞는지, 안 맞는지 확인하자
'''


def test(nums):
    nums = [k for k in nums]  # 이렇게 하면 한 번에 문자열로 받은 내용을 하나씩 잘라서 리스트로 넣을 수 있다.

    start_idx = 0
    end_idx = len(nums) - 1

    while start_idx < end_idx:
        if nums[start_idx].isalpha() or nums[start_idx].isdigit():
            pass
        else:
            start_idx += 1

        if nums[end_idx].isalpha() or nums[end_idx].isdigit():
            pass
        else:
            end_idx -= 1

        if nums[end_idx].lower() == nums[start_idx].lower():
            start_idx += 1; end_idx -= 1
        else:
            return False
    return True

if __name__=="__main__":
    print(test(['tomot ']))