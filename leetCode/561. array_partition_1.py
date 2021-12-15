'''
2개씩 그룹을 만들고, 각 그룹 중 가장 작은 값의 합이 최대가 되는 값을 구해야 한다.

순서대로 한 후에, 1개씩 징검다리로 합한 값이 최대 값임을 찾음.
'''

def test(nums):
    nums.sort()
    result = []
    for i in range(0, len(nums), 2):
        result.append(nums[i])
    return sum(result)

if __name__=="__main__":
    print(test([6,2,6,5,1,2]))
    print(test([1,4,3,2]))