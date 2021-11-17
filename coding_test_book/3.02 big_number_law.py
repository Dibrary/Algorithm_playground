'''
첫 번째 숫자는 자연수,
두 번째 숫자는 구성해야할 원소 갯수
세 번째 숫자는 초과할 수 없는 값

'''


def test():
    print("문제에서 언급한 N, M, K값을 입력하세요.")
    n, m, k = list(input().split())
    print("수 배열을 입력하세요")
    nums = [int(x) for x in input().split()]
    nums.sort()

    if len(nums) < int(n) or len(nums) > int(n):
        return -1

    max_value = nums.pop()
    second_value = nums.pop()

    cnt = 0
    result = 0
    tmp = 0
    while cnt < int(m):
        if tmp <= int(k) - 1:
            result += max_value
            tmp += 1
        else:
            result += second_value
            tmp = 0
        cnt += 1

    return result

if __name__=="__main__":
    print(test())