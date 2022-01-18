
'''
이 문제의 핵심은 지금 '가져온 카드의 왼쪽 끝과, 오른쪽 끝 값' 으로 보인다.
이 값에 따라 새로 가져온 카드의 위치가 배정된다.

ord("A") = 65다
'''


n = int(input())

for _ in range(n):
    result = []

    length = int(input())
    arr = list(input().split())
    result.append(arr.pop(0))

    while True:
        print(arr)
        if arr == []:
            break
        value = arr.pop(0)
        left = ord(result[0])
        right = ord(result[-1])
        if ord(value) <= left:
            result.insert(0, value)
        elif ord(value) > right:
            result.insert(len(result), value)
        else:
            result.append(value)
    print("".join(map(str,result)))
