# n = int(input())
#
# tmp1 = n//5
# tmp11 = (n%5)//3
#
# tmp2 = n//3
# tmp22 = (n%3)//5
#
# if tmp1*5+tmp11*3 == n and tmp2*3+tmp22*5 == n:
#     print(min(tmp1+tmp11, tmp2+tmp22))
# elif tmp1*5+tmp11*3 == n and tmp2*3+tmp22*5 != n:
#     print(tmp1+tmp11)
# elif tmp1*5+tmp11*3 != n and tmp2*3+tmp22*5 == n:
#     print(tmp2+tmp22)
# else:
#     print(-1)

# 위 코드는 11에서 예외가 남. 동적계획법으로 해결해야 할 거 같은데...


n = int(input())

tmp = set()

for i in range(n//3+1):
    if (n-(i*3))%5 == 0:
        tmp.add(i+(n-(i*3))//5)
    else:
        tmp.add(-1)

if tmp == {-1}:
    print(-1)
else:
    tmp.remove(-1)
    print(min(tmp))



