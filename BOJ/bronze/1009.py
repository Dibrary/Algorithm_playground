# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     print("%d"%((a**b)%10))
    # 이건 시간 초과 걸린다.

# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     if a == 1:
#         print(1)
#     elif a == 2:
#         tmp = b%4
#         table = [0,2,4,8,6]
#         print("%d"%(table[tmp]))
#     elif a == 3:
#         pass
         #  근데 이런 방식으로는 100까지 못 한다.

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        print(1)
    elif a == 2:
        if b%4 == 0:   print(6)
        elif b%4 == 1: print(2)
        elif b%4 == 2: print(4)
        elif b%4 == 3: print(8)
    elif a == 3:
        if b%4 == 0:   print(1)
        elif b%4 == 1: print(3)
        elif b%4 == 2: print(9)
        elif b%4 == 3: print(7)
    elif a == 4:
        if b%2 == 0:   print(6)
        else:          print(4)
    elif a == 5:       print(5)
    elif a == 6:       print(6)
    elif a == 7:
        if b%4 == 0:   print(1)
        elif b%4 == 1: print(7)
        elif b%4 == 2: print(9)
        elif b%4 == 3: print(3)
    elif a == 8:
        if b%4 == 0:   print(6)
        elif b%4 == 1: print(8)
        elif b%4 == 2: print(4)
        elif b%4 == 3: print(2)
    elif a == 9:
        if b%2 == 0:   print(1)
        else:          print(9)


# 위 값들을 구하는데 사용한 코드
a = 7
for i in range(1, 10):
    value = str(a**i)
    print(value[-1], i)
