
'''
ord('a') 하면 97 나온다.
즉 ord('a')-96 = 1이 된다.

ord('A') 하면 65 나온다.

이 문제의 핵심은 입력을 최소 신장 트리 알고리즘을 쓸 수 있는 형태로 변형하는 것이다.
'''


n = int(input())

arr = []
for _ in range(n):
    # values = list(map(int, input().split()))
    # if len(values) == 3:
    #     start, end, begin = values[0], values[1], values[2]
    # else: # 하나가 0인 경우다.
    #     pass # 진입점이 0인 경우는 어떻게 처리해야 하나?

    arr.append(list(input())) # 입력을 곧바로 리스트에 담아보는 것이다.

change_arr = []
print(arr)
for s in arr:
    tmp = []
    for k in s:
        if k.isupper():
            tmp.append(ord(k)-38)
        elif k.islower():
            tmp.append(ord(k)-96)
        elif k == '0':
            tmp.append(0)
    change_arr.append(tmp)
print(tmp)









