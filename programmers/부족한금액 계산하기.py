
'''
N번 째 이용하면 N배의 price를 받아야 함.
'''


# def solution(price, money, count):
#     total_need = 0
#     for i in range(1, count+1):
#         total_need += price * i
#     return total_need - money
#
# print(solution(3,20,4))

# 위 코드는 딱 1개 실패함. 23개 항목 중.
# 위 return방식으로는 돈이 남으면 -값이 반환됨.


def solution(price, money, count):
    total_need = 0
    for i in range(1, count+1):
        total_need += price * i
    return total_need - money if (total_need - money) > 0 else 0


## 다른 사람 코드 ##

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))





def solution(price, money, count):
    total = (price * (1+count) * count / 2)
    return total - money if total > money else 0



