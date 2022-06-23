
# def maxProfit(prices):
#     result = -100000000
#     for i in range(0, len(prices)-1):
#         for j in range(i+1, len(prices)):
#             value = prices[j]-prices[i]
#             if value >= result:
#                 result = value
#
#     if result < 0:
#         return 0
#     else:
#         return result
#
#
# print(maxProfit([7,1,5,3,6,4]))

# 답은 맞는데 시간초과가 걸림. (입력 데이터 10**5개)

import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices: # 중요한 것은 for문 한 개 쓴 것.

        min_price = min(min_price, price) # 처음 값부터 설정된다. # 전체 값 중 최소 값이면 갱신.
        profit = max(profit, price - min_price) # 전체 값 중 현재 설정된 최소값과 차이가 가장 크면 갱신.

    return profit

### 다른 사람 코드 ###

class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit



# 아래껀 시간 꽤 걸린 풀이

class Solution:
    def maxProfit(self, prices):
        last_index=len(prices)-1
        pointer=prices[-1]
        max_profit=0

        for i in range(last_index-1, -1, -1):
            if pointer<=prices[i]:
                pointer=prices[i]
            else:
                max_profit=max(pointer-prices[i],max_profit)
        return max_profit





