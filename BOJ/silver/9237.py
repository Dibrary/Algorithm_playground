
'''
이 문제의 핵심은 '이장은 최대 일 수 다음날에 온다'는 것과.
최대 일 수가 가장 적게 되게 해야 한다는 것이다.
'''

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(0, len(arr)):
    arr[i] = arr[i]+(i+1)
print(max(arr)+1)

