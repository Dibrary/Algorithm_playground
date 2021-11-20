'''
큰 수부터 작은 수대로 나열하기
'''

def test():
    print("갯수를 입력하세요")
    n = int(input())
    print("갯수 만큼의 수를 입력하세요")
    nums = []
    for s in range(0, n):
        nums.append(int(input()))

    for i in range(0, len(nums)-1):
        min_idx = i
        for j in range(i, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def test2():
    print("갯수를 입력하세요")
    n = int(input())
    print("갯수 만큼의 수를 입력하세요")
    nums = []
    for s in range(0, n):
        nums.append(int(input()))

    return sorted(nums)

if __name__=="__main__":
    print(test())
    print(test2())