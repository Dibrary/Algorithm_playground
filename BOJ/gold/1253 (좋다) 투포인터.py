
'''
시간복잡도가 O(n^2)인 알고리즘을 사용하면 최종 복잡도가 N^3이 된다.
시간복잡도는 최소 O(nlogn)보다 작아야 함. => 그래서 투 포인터가 적합하다.

자기 자신을 제외해야 한다. (다른 두 수 두 개의 합으로 나타내는지 판단)
'''

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0

for k in range(n):
    find = arr[k]
    i = 0
    j = n-1

    while i < j:
        if (arr[i] + arr[j]) == find:
            if (i != k) and (j != k):
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j += 1
        elif (arr[i] + arr[i]) < find:
            i += 1
        else:
            j -= 1
print(result)

# 위 코드 책에 나온것 파이썬으로 옮긴건데 자꾸 0만 나옴. 왜?




## 다른 사람 코드 ##
import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    ans = 0

    for i in range(N):
        tmp = arr[:i] + arr[i + 1:]
        left, right = 0, len(tmp) - 1
        while left < right:
            t = tmp[left] + tmp[right]
            if t == arr[i]:
                ans += 1
                break
            if t < arr[i]: left += 1 # t 를 증가시켜야 하므로 left 증가
            else: right -= 1 # t 를 감소시켜야 하므로 right 감소
    print(ans)











def solve():
    cnt = 0
    nums.sort()
    for i in range(len(nums)):
        if search(i, nums[i]):
            cnt += 1
    print(cnt)


# 좋은 수가 들어있는지 탐색하는 함수
def search(i, target):
    temp = nums[:i] + nums[i+1:]  # 타겟이 되는 nums[i]를 제외하고 탐색
    # print(temp)
    left = 0
    right = n-2  # 마지막 인덱스 n-1에서 타겟값 하나 더 빼서 n-2
    while left < right:
        sum = temp[left] + temp[right]
        if target < sum:
            right -= 1
        elif target > sum:
            left += 1
        else:
            # print(i,target)
            return True
    return False


import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
solve()









import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i, num in enumerate(arr):
    temp = arr[:i]+arr[i+1:]
    left, right = 0, len(temp)-1
    while left < right:
        if temp[left]+temp[right] > num:
            right -= 1
        elif temp[left]+temp[right] < num:
            left += 1
        else:
            result += 1
            break

print(result)