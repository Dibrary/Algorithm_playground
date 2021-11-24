'''
회전 횟수를 억단위로 해도 에러나지 않는 코드
'''

def test(nums, k):
    result = [0] * len(nums)
    k = k%len(nums) # 이거 하나로 큰 수를 len보다 작은 수로 만들어 준다.
    idx = k

    for i in nums:
        if idx > len(nums) - 1:
            idx -= len(nums)
        result[idx] = i
        idx += 1

    return result

if __name__=="__main__":
    print(test([7,5,9,4,2,6],8000000023))

