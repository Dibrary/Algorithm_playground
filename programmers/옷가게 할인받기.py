# def solution(price):
#     if price >= 500000:
#         return int(price*0.8)
#     elif price >= 300000:
#         return int(price*0.9)
#     else:
#         return int(price*0.95)

# 위 코드 85.7점 받음 .. 왜?

def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    else:
        return price
# 10만원 이하는 또 별개다.

