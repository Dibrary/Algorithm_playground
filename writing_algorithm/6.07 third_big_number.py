'''
3번째로 큰 수를 반환하자.
입력 값이 3개보다 작다면, 큰 수를 반환하자.
'''

def test():
    print("input array")
    nums = [int(x) for x in input().split()]
    nums.sort()

    return nums[-3] if len(nums) > 3 else max(nums)

if __name__=="__main__":
    print(test())