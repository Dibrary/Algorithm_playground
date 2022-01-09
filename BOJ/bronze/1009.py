n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print("%d"%((a**b)%10))
    # 이건 시간 초과 걸린다.

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        print(1)
    elif a == 2:
        tmp = b%4
        table = [0,2,4,8,6]
        print("%d"%(table[tmp]))
    elif a == 3:
        pass
         #  근데 이런 방식으로는 100까지 못 한다.