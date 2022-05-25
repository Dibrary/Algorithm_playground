
def func(n):
    x = 0
    y = 0

    cnt = 0

    direction = 1

    nx = 1
    ny = 1

    while cnt < n:
        for i in range(nx):
            if direction == 1:
                x += 1
            else:
                x -= 1
            cnt += 1
            if cnt == n:
                print(y, x) # 왜인진 모르겠으나 출력에서 x와 y가 바뀌어야됨;
                return
        nx += 1
        for j in range(ny):
            if direction == 1:
                y += 1
            else:
                y -= 1
            cnt += 1
            if cnt == n:
                print(y, x)
                return
        ny += 1
        if direction == 1:
            direction = -1
        else:
            direction = 1

n = int(input())
func(n)






