def test():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()

    cnt = 0

    while len(nums) != 0:
        value = nums[-1]
        for i in range(0, value): # 최대 숫자 값 만큼 list에서 제거함. (그룹으로 취급)
            nums.pop()
        cnt += 1
    print(cnt)

def answer():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    result = 0
    count = 0
    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0
    print(result)

if __name__=="__main__":
    test()
    # answer() # 테스트 값 확인 용