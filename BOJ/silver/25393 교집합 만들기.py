
'''
문제 이해가 안 되네, 예제에서 4 6은, 결국 3개 모두 가능할텐데 출력이 2다.

'''
n = int(input())
tmp = dict()

for _ in range(n):
    l, r = map(int, input().split())

    for k in range(l, r+1):
        if k not in tmp:
            tmp[k] = 1
        else:
            tmp[k] += 1
print(tmp)

q = int(input())
for _ in range(q):
    result = 1e9
    l, r = map(int, input().split())

    for k in range(l, r+1):
        if result >= tmp[k]:
            result = tmp[k]
    if result == 1e9:
        print(-1)
    else:
        print(result)







